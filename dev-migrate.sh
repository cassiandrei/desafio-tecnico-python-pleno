#!/bin/bash

docker-compose -f docker-compose-dev.yml run \
  --rm \
  web \
  python manage.py makemigrations


