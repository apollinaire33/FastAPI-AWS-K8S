FROM python:3.10 AS base

WORKDIR usr/src/post
COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .
CMD alembic upgrade head

FROM base as dev
CMD uvicorn post.main:app --reload  --host 0.0.0.0
