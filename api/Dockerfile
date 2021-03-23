FROM python:3.8.3-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev python3-dev musl-dev gcc

# Pillow dependencias
RUN apk add zlib-dev jpeg-dev libjpeg

# dependencies
RUN apk add --no-cache --virtual .build-deps gcc libc-dev libxslt-dev && \
    apk add --no-cache libxslt && \
    apk del .build-deps

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade Pillow
RUN pip install -r /requirements.txt

RUN apk add python3-dev build-base linux-headers pcre-dev
RUN pip install https://github.com/unbit/uwsgi/archive/uwsgi-2.0.zip#egg=uwsgi


# Create the app user without root prvilegies
RUN addgroup -S app && adduser -S app -G app

# Create the appropriate directories
ENV APP_HOME=/docker_api
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles

WORKDIR $APP_HOME

# copy project
COPY . $APP_HOME

# chown all the files to the app user


# copy entrypoint.sh
COPY ./scripts /scripts

RUN chmod +x /scripts/*

USER app

# run entrypoint.sh
CMD ["/scripts/entrypoint.sh"]

