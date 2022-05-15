# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /app
COPY /src ./src
COPY /config ./config
RUN pip install -r src/requirements.txt
EXPOSE 5000
CMD python src/main.py