import datetime
import math

from flask import Markup
from peewee import Model, TextField, DateTimeField

from app import db


class Quote(Model):
    content = TextField()
    date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

    def html(self):
        return Markup(self.content.replace('\n', '<br>'))

    @classmethod
    def paged(cls, page, page_size):
        quotes = Quote.select().order_by(Quote.date.desc())
        page_count = math.ceil(quotes.count() / page_size)
        return quotes.offset(page * page_size).limit(page_size), page_count
