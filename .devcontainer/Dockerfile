ARG VARIANT="3.11"
FROM mcr.microsoft.com/devcontainers/python:0-${VARIANT}

RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends dos2unix
