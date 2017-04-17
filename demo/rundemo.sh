#!/bin/sh
set -e
rm /tmp/tmc2.db
sqlite3 /tmp/tmc2.db < demo.sql
make -C .. run
