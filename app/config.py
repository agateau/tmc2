DATABASE = '/tmp/tmc2.db'
DEBUG = False

# By default we only listen on localhost. Set this to '0.0.0.0' to accept
# requests from any interface
HOST = '127.0.0.1'
PORT = 5000

# How many quotes per page
PAGE_SIZE = 10

# How should dates be formatted. The format is defined in the man page for
# strftime.
DATE_FORMATS = {
    'en_US': '%B %d, %Y',
    'fr_FR': '%d %B %Y',
}

# This must be set to a locale recognized by your Python installation. If you
# define it to something other than one of the keys of `DATE_FORMATS`, define a
# `DATE_FORMATS` entry for the locale you picked.
LOCALE = 'en_US'

# To customize the configuration, create a local configuration file and point
# the TMC2_CONFIG environment variable to it.
