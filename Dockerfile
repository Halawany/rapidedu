FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /rapidedu

COPY Pipfile Pipfile.lock /rapidedu/
RUN pip install pipenv && pipenv install --system

COPY . /rapidedu/