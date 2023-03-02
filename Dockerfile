FROM python:3.10.9

RUN mkdir /app
COPY ./requirements.txt /app/requirements.txt
COPY . /app
WORKDIR /app
RUN pip install -r /app/requirements.txt