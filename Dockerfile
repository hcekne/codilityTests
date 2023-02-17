FROM python:3.8-alpine

RUN apk update
# taking out the --no-cache option
RUN apk add bash

RUN apk add shadow
#RUN chsh -s /bin/bash

RUN apk add nano
# RUN apk add py3-pip

RUN python3.8 -m ensurepip 
RUN python3.8 -m pip install --upgrade pip

RUN mkdir /app
COPY . /app
WORKDIR /app
ENV PYTHONPATH="/app"


RUN python3.8 -m pip install -r requirements.txt

ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache

RUN python3.8 -m pip install -e /app/src/


CMD ["/bin/bash"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]

#CMD ["/bin/sh"]
