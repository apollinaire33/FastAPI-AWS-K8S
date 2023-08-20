FROM python:3.10 AS base

WORKDIR usr/src/user
COPY ./requirements ./requirements

RUN pip install --no-cache-dir --upgrade -r requirements/base.txt -r requirements/prod.txt

COPY . .
CMD alembic upgrade head

FROM base as prod

CMD gunicorn user.main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0
EXPOSE 8000
