FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /application
WORKDIR "/application"
RUN apt-get update \
    && apt-get -y install apt-utils \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*
ADD requirements.txt /application/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh