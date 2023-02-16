#!/bin/bash

# Image builder script for devcontainer

# took out the --no-cache option

docker build . -f "$(pwd)"/Dockerfile --progress=plain --no-cache -t plain_alpine_python_38_image
