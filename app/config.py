DATABASE = '/tmp/tmc2.db'
DEBUG = False

# By default we only listen on localhost. Set this to '0.0.0.0' to accept
# requests from any interface
HOST = '127.0.0.1'
PORT = 5000

# How many quotes per page
PAGE_SIZE = 10

# How should dates be formatted. The format is defined in
# http://arrow.readthedocs.io/en/latest/index.html#tokens
DATE_FORMATS = {
    'en_US': 'MMMM D, YYYY',
    'fr_FR': 'D MMMM YYYY',
}

# The locale to use. Must be one of the keys defined in DATE_FORMATS
LOCALE = 'en_US'

# To customize the configuration, create a local configuration file and point
# the TMC2_CONFIG environment variable to it. For example to use TMC2 in
# French, define LOCALE to 'fr_FR'.
