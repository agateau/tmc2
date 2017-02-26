#!/usr/bin/env python3
from app import app
from models import Quote
import views  # noqa


if __name__ == '__main__':
    Quote.create_table(True)
    app.run(host='0.0.0.0', debug=True)
