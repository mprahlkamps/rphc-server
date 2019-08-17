from .shared import *

with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

DEBUG = False

# TODO: Add allowed hosts
ALLOWED_HOSTS = []

SIMPLE_JWT['SIGNING_KEY'] = SECRET_KEY

# TODO: Add real DB
DATABASES = {}

# TODO: Add cors clients
CORS_ORIGIN_WHITELIST = []
