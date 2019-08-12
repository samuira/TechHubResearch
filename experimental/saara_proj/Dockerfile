FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /saara_proj
WORKDIR /saara_proj
RUN apt-get update \
    && apt-get -y install apt-utils\
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*
ADD requirements.txt /saara_proj/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /saara_proj
RUN chmod +x /saara_proj