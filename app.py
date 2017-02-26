from flask import Flask
from peewee import SqliteDatabase

app = Flask(__name__)
app.config.from_object('config')
app.config.from_envvar('TMC2_CONFIG')
db = SqliteDatabase(app.config['DATABASE'], threadlocals=True)
