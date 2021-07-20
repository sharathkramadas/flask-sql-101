FROM python:rc-alpine3.13
RUN apk update
RUN apk add gcc g++ mariadb-connector-c-dev
WORKDIR /webapp
COPY app.py app.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh
