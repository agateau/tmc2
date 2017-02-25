import datetime

from flask import Markup
from peewee import Model, TextField, DateTimeField

from app import db


class Quote(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

    def html(self):
        return Markup(self.content)

    @classmethod
    def public(cls):
        return Quote.select().order_by(Quote.timestamp.desc())
