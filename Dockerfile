# An image for TMC2. Start it with a directory bound to /data. There must be a
# `config.py` file in this directory for TMC2 configuration.
FROM alpine
MAINTAINER Aurélien Gâteau <mail@agateau.com>

RUN \
    apk add --no-cache bash python3 \
    && pip3 install --upgrade pip \
    && mkdir -p /app

COPY requirements.txt /app/
RUN pip3 install -r /app/requirements.txt

COPY app /app

VOLUME /data
ENV TMC2_CONFIG "/data/config.py"

EXPOSE 5000

ENTRYPOINT ["/app/main.py"]
