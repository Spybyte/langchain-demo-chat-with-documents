import sys
import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
from typing import Any
from langchain.chat_models import ChatOpenAI
from langchain.schema import Document
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
import os


st.set_page_config(page_title="Documentation Chatbot", page_icon=":robot_face:")
st.markdown(
    "<h2 style='text-align: center;'>BeData Catalog Documentation Chatbot</h1>", unsafe_allow_html=True
)

load_dotenv()


def init_model(model: str) -> Any:
    # Load the LangChain.
    persist_directory = os.environ["CHROMADB_FOLDER"]
    embedding = OpenAIEmbeddings()  # type: ignore [call-arg]
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)

    llm = ChatOpenAI(model_name=model, temperature=0.0, max_tokens=256)  # type: ignore [call-arg]  # noqa: E501
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        chain_type="stuff",
        retriever=vectordb.as_retriever(),
        return_source_documents=True,
    )
    return chain


def get_sources(documents: Document) -> set[str]:
    return set([doc.metadata.get("source") for doc in documents])  # type: ignore [attr-defined] # noqa: E501


def ask(query: str) -> tuple[str, str, set[str]]:
    chat_history = list(zip(st.session_state["past"], st.session_state["generated"]))

    result = qa({"question": query, "chat_history": chat_history})
    answer = result["answer"]
    sources = get_sources(result["source_documents"])
    chat_history.append((query, answer))
    return query, answer, sources


def initialize() -> None:
    if "generated" not in st.session_state:
        st.session_state["generated"] = []
    if "sources" not in st.session_state:
        st.session_state["sources"] = []
    if "past" not in st.session_state:
        st.session_state["past"] = []


def clear_all() -> None:
    st.session_state["generated"] = []
    st.session_state["past"] = []
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]


clear_button = None
counter_placeholder = None


initialize()
if clear_button:
    clear_all()
model = model = os.environ["OPENAI_MODEL"]
qa = init_model(model=model)


# container for text box
container = st.container()
# container for chat history
response_container = st.container()

with container:
    with st.form(key="input", clear_on_submit=True):
        user_input = st.text_area("You:", key="input", height=100)
        submit_button = st.form_submit_button(label="Send")

    if submit_button and user_input:
        query, answer, sources = ask(user_input)
        st.session_state["past"].append(query)
        st.session_state["generated"].append(answer)
        st.session_state["sources"].append(sources)


if st.session_state["generated"]:
    with response_container:
        for i in range(len(st.session_state["generated"]) - 1, -1, -1):
            message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
            message(st.session_state["generated"][i], key=str(i))
            st.write(f"Sources:    {st.session_state['sources'][i]}")
