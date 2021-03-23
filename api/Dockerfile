# pull official base image
FROM python:3.6.2-alpine

# set work directory
RUN mkdir /docker_api
WORKDIR /docker_api

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# Pillow dependencias
RUN apk add zlib-dev jpeg-dev libjpeg

RUN apk add --no-cache --virtual .build-deps libc-dev libxslt-dev zlib  && \
    apk add --no-cache libxslt && \
    pip install --no-cache-dir lxml>=3.5.0 && \
    apk del .build-deps

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /docker_api/requirements.txt

RUN apk add python3-dev build-base linux-headers pcre-dev
RUN pip install https://github.com/unbit/uwsgi/archive/uwsgi-2.0.zip#egg=uwsgi

RUN pip install -r requirements.txt

# copy entrypoint.sh

COPY scripts/entrypoint.sh /docker_api/entrypoint.sh

RUN chmod +x entrypoint.sh

# copy project
COPY . /docker_api

# run entrypoint.sh
ENTRYPOINT ["/docker_api/entrypoint.sh"]