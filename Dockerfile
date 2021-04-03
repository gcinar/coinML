FROM python:3.8

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="~/.poetry/bin:${PATH}"

#this dockerfile is intended to be used with VSCode + Remote-Containers extension
#due to .devcontainer/.devcontainer.json VSCode will prompt the developer 
#to open the current folder in a remote container. This will create a attached volume
#which is your repo under /workspaces/coinML
#WORKDIR /workspaces/coinML
#RUN ~/.poetry/bin/poetry install