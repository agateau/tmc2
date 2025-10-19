# An image for TMC2, serving it using waitress on port 8000,
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

# This version of Python is outdated, but that's the one known to work with the
# app dependencies right now. Need to refresh it.
FROM python:3.7-slim
LABEL org.opencontainers.image.authors="mail@agateau.com"

RUN \
    apt-get update -y \
    && apt-get install \
        -y --no-install-recommends \
        make

COPY requirements.txt Makefile /opt/
RUN make -C /opt venv
ENV PATH=/opt/venv/bin:$PATH
RUN python -m pip install waitress

COPY app /opt/app
RUN make -C /opt compile_trans

USER www-data
WORKDIR /opt/app

ENTRYPOINT ["waitress-serve", "--port", "8000", "main:app"]
