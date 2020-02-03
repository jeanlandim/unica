FROM python:3.7
ENV PYTHONBUFFERED 1
RUN mkdir /unica
WORKDIR /unica
ADD . /unica

RUN pip3 install -r vitaemanager/requirements.txt 
