FROM python:3.8-alpine

RUN apk update
RUN apk add --no-cache bash

RUN apk add --no-cache shadow
#RUN chsh -s /bin/bash

RUN apk add nano
# RUN apk add py3-pip

RUN python3.8 -m ensurepip 
RUN python3.8 -m pip install --upgrade pip

RUN mkdir /app
WORKDIR /app
ENV PYTHONPATH="/app"

COPY requirements.txt /app
RUN python3.8 -m pip install -r requirements.txt

ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache
COPY src/ /app/src/
RUN python3.8 -m pip install -e src


CMD ["/bin/bash"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]

#CMD ["/bin/sh"]
