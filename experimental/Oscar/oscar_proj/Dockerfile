FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /oscar_proj
WORKDIR "/oscar_proj"
RUN apt-get update \
    && apt-get -y install apt-utils\
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*
ADD requirements.txt /oscar_proj/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /oscar_proj
RUN chmod +x /oscar_proj