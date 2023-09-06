FROM python:3.10.5

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./requirements.txt /code/requirements.txt

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app