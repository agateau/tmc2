import os

from flask import Flask
from peewee import SqliteDatabase

app = Flask(__name__)
app.config.from_object('config')
if 'TMC2_CONFIG' in os.environ:
    app.config.from_envvar('TMC2_CONFIG')
db = SqliteDatabase(app.config['DATABASE'], threadlocals=True)
