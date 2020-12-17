FROM python:3.9-alpine

RUN apk add --no-cache --update build-base libffi-dev openssl-dev &&\
    pip install --prefer-binary poetry
