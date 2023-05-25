FROM python:3.10-slim-buster
LABEL maintainer="github.com/shellyguns"

ENV PYTHONUNBUFFERED 1

COPY . .
WORKDIR /app

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /app/requirements.txt && \
    apt-get update && apt-get install ffmpeg libsm6 libxext6  -y && \
    apt install libgl1-mesa-glx && \
    adduser \
        --disabled-password \
        --no-create-home \
        model-user

ENV PATH="/py/bin:$PATH"

USER model-user