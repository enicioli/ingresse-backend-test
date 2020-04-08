FROM tiangolo/meinheld-gunicorn-flask:python3.7

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

ENV MODULE_NAME=run