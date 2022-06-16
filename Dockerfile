FROM python:alpine AS base

WORKDIR /app

COPY requirements.txt .
COPY app.py .
RUN pip3 install -r requirements.txt

RUN export FLASK_APP=app

CMD ["flask", "run", "--host=0.0.0.0"]
EXPOSE 5000
