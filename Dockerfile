FROM python:3.9

WORKDIR /code
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="~/.poetry/bin:${PATH}"
RUN git clone https://github.com/gcinar/coinML.git

WORKDIR /code/coinML
RUN poetry install