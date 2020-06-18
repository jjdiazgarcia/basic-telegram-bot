FROM python:alpine3.12

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

EXPOSE 8080

CMD ["python", "bot.py"]