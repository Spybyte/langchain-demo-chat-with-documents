# LangChain: Chat with documents test case

## Requirements

This project was written using Python 3.11. For convenience you can run the whole project in a dev container using Visual Studio Code.

1. Install Dock
2. Open the project in VS Code
3. Build the dev container from VS Code menu
4. Reload window from VS Code menu


## Initialization

You need to create a .env in the root folder. You can use the .env.SAMPLE as a template:

```cp .env.SAMPLE .env```

Edit .env and set the `OPENAI_API_KEY` variable with you openAI api key. The other variables do not need to be changed.

For building the vector database there are two options:

1. Copy your PDF documents in the folder called `docs` on the root level of this project. You can copy the whole directory structure into this folder.
2. Run the Jupyter Notebook `ingest.ipynb` from the src folder to create the vector database.
3. Run the Jupyter Notebook `ask.ipynb` from the src folder to query your documents


## Running

To start the chat client run `bash scripts/run.sh` which will start streamlit. Alternatively you can just use `streamlit run src/app.py`.
