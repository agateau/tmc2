# An image for TMC2, serving it using uwsgi on port 8000,
# running as uid 33:33 (www-data on Debian).
#
# Mount a volume in it containing the configuration and database,
# and set $TMC2_CONFIG to the path to the configuration file.
#
# For example create a data dir like this:
#
# tmc2-data
#   config.py
#   db
#     tmc2.db
#
# - Make `db` and its content owned by uid 33:33 (www-data:www-data on Debian)
# - Make sure `config.py` contains a line which says:
#
#     DATABASE = "/data/db/tmc2.db"
#
# - Mount `tmc2-data` as `/data` in the container
# - Set $TMC2_CONFIG to `/data/config.py`

# This version of Debian is outdated, but that's the one known to work with the
# app dependencies right now. Need to refresh it.
FROM debian:10
MAINTAINER Aurélien Gâteau <mail@agateau.com>

RUN \
    apt-get update -y \
    && apt-get install \
        -y --no-install-recommends \
        python3 \
        python3-venv \
        uwsgi \
        uwsgi-plugin-python3 \
        make

COPY requirements.txt Makefile /opt/
RUN make -C /opt venv

COPY app /opt/app
COPY docker /opt/docker
RUN make -C /opt compile_trans

USER www-data

ENTRYPOINT ["uwsgi", "--ini", "/opt/docker/uwsgi.ini"]
