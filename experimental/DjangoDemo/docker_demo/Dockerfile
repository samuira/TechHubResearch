FROM python:3.5

ENV PYTHONUNBUFFERED 1

RUN mkdir /application
WORKDIR "/application"

# Install python mysql client
RUN apt-get update \
    && apt-get -y install libmysqlclient-dev libpq-dev postgresql postgresql-contrib\
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

ADD requirements.txt /application/
RUN pip install -r requirements.txt









































# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
# FROM python:3.5

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
# ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
# RUN mkdir /docker_project

# Set the working directory to /music_service
# WORKDIR /docker_project

# Copy the current directory contents into the container at /music_service
# ADD . /docker_project/

# Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt