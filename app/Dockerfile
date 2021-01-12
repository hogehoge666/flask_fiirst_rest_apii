FROM python:3.8-slim-buster

EXPOSE 5000

WORKDIR /app

ADD . ./

# required for MySQL
# RUN apk add --no-cache gcc libc-dev libffi-dev openssl-dev
RUN python3 -m pip install -r requirements.txt

# nice to have for sqlite3
RUN apt-get update
RUN apt-get install sqlite3

ENV TODOAPI_ENV=docker
ENV TODOAPI_REMOTE_DEBUG=on

CMD ["python3", "main.py"]