FROM python:3.8-slim AS base

WORKDIR /src

RUN apt update

COPY requirement.txt ./requirement.txt

RUN pip install -r ./requirement.txt

COPY . .

EXPOSE 3000

ENTRYPOINT ["bash", "-c", "gunicorn --bind 0.0.0.0:3000 wsgi:app"]



