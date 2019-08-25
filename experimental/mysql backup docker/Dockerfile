FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /karakira_proj
RUN mkdir /mysql
RUN mkdir /dbr
RUN mkdir /dbb
WORKDIR /karakira_proj
RUN apt-get update \
    && apt-get -y install apt-utils\
    && apt-get -y install libstdc++6 && apt-get -y install python-setuptools && apt-get -y install python3-dev\
    && apt-get -y install build-essential && apt-get -y install gcc && apt-get -y install libxml2-dev\
    && apt-get -y install libxslt1-dev && apt-get -y install zlib1g-dev\
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*
ADD requirement.txt /karakira_proj/
RUN pip install --upgrade pip
RUN pip install -r requirement.txt
COPY . /karakira_proj
#RUN cd kpi && pip install -e . && KPI migrate -o True
RUN chmod +x /karakira_proj