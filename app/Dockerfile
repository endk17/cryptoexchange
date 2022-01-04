###########
# BUILDER #
###########

# pull official base image
FROM python:3.10.1-slim-buster as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install gcc \
  && apt-get clean

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

# # lint
# COPY . .
# RUN pip install black==21.12b0 flake8==4.0.1 isort==5.10.1
# RUN flake8 .
# RUN black . --check --exclude=migrations
# RUN isort . --check-only


#########
# FINAL #
#########

# pull official base image
FROM python:3.10.1-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG False
ARG SECRET_KEY
ENV SECRET_KEY $SECRET_KEY
ARG PORT
ENV PORT $PORT
ARG COINBASE_COMMERCE_API_KEY
ENV COINBASE_COMMERCE_API_KEY $COINBASE_COMMERCE_API_KEY
# ARG DJANGO_ALLOWED_HOSTS
# ENV DJANGO_ALLOWED_HOSTS $DJANGO_ALLOWED_HOSTS

# install system dependencies
RUN apt-get update \
  && apt-get -y install gcc \
  && apt-get clean

# install dependencies
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy project
COPY . .

# collect static files for local dev
RUN python manage.py collectstatic --noinput

# add and run as non-root user
RUN adduser --disabled-password myuser
USER myuser

# run gunicorn
CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT