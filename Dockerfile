FROM ubuntu:20.04

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN apt update
RUN apt install python3-pip -y
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["/usr/bin/python3", "main.py"]