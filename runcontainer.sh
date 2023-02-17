#!/bin/bash

# use this option when running in detached mode
#--user "$(id -u)" --group-add users \
#-e NB_USER="$(whoami)" \
#    -e NB_UID="$(id -u)" \
#    -e NB_GID="$(id -g)"  \
#    -e CHOWN_HOME=yes \
#    -e CHOWN_HOME_OPTS="-R" \
#    -w "/home/$(whoami)" \
# use user shiny to have it run as the shiny user

docker run -it --rm \
    -p 3838:3838 \
    --user root \
    -v "${PWD}/src":/src/ \
        plain_alpine_python_38_image
