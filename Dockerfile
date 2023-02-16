FROM python:3.8-alpine

RUN apk update
RUN apk add --no-cache bash

RUN apk add --no-cache shadow
#RUN chsh -s /bin/bash

ENTRYPOINT ["tail", "-f", "/dev/null"]

#CMD ["/bin/sh"]
