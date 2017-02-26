FROM alpine
MAINTAINER Aurélien Gâteau <mail@agateau.com>

ADD . /app

RUN \
    apk add --no-cache bash python3 \
    && pip3 install --upgrade pip \
    && pip3 install -r /app/requirements.txt

EXPOSE 5000

ENTRYPOINT ["/app/main.py"]
