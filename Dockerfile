#base image
FROM python:3.10.9-alpine3.17

#maintainer
LABEL Author="MatiasColl"

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONBUFFERED 1

#directory to store app source code
RUN mkdir /corbis

#switch to /app directory so that everything runs from here
WORKDIR /corbis

#copy the app code to image working directory
COPY ./corbis /corbis

#let pip install required packages
RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && python manage.py makemigrations \
    && python manage.py migrate 
