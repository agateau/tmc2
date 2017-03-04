#!/usr/bin/env python3
import argparse
import json
import sys

import arrow

from app import db
from models import Quote


DESCRIPTION = """\
Import quotes from a JSON file. See README.md for details of the format.
"""


def create_insert_list(quotes):
    for quote in quotes:
        date = arrow.get(quote['date']).datetime.strftime('%Y-%m-%d %H:%M:%S')
        text = quote['text']
        yield dict(date=date, content=text)


def do_import(quotes):
    lst = create_insert_list(quotes)
    with db.atomic():
        Quote.insert_many(lst).execute()


def main():
    parser = argparse.ArgumentParser()
    parser.description = DESCRIPTION

    parser.add_argument('-c', '--clean', action='store_true',
                        help='Delete all quotes before importing. Dangerous!')

    parser.add_argument('json_file')

    args = parser.parse_args()

    with open(args.json_file) as f:
        quotes = json.load(f)['quotes']

    if args.clean:
        Quote.delete().execute()
    do_import(quotes)

    return 0


if __name__ == '__main__':
    sys.exit(main())
# vi: ts=4 sw=4 et
