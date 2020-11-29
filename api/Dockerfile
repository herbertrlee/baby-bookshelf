FROM python:3.7-slim

RUN mkdir /app

WORKDIR /app

ADD requirements.txt /app

RUN pip install -r requirements.txt

ADD . .

EXPOSE 8080

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "main:app"]
