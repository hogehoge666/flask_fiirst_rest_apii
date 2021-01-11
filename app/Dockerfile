FROM python:3.8-alpine

LABEL Name=todoapi Version=0.0.1

EXPOSE 5000

ENV TODOAPI_ENV=docker
ENV TODOAPI_REMOTE_DEBUG=on

WORKDIR /app

ADD . ./

RUN python3 -m pip install -r requirements.txt
RUN apk add sqlite

CMD ["python3", "main.py"]