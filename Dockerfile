FROM python:3.6-onbuild

RUN mkdir -p /app

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip -r requirements.txt

COPY . .
