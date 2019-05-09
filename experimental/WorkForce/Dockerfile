FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /workforce
WORKDIR "/workforce"
RUN apt-get update \
    && apt-get -y install apt-utils\
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*
ADD requirements.txt /workforce/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /workforce
RUN chmod +x /workforce