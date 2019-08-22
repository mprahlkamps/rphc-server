from .shared import *

SECRET_KEY = 'zd^g9t22n&56=ymtctale3yu0+d9o1y+(rkr^t2+y*iiz^69&a'
SIMPLE_JWT['SIGNING_KEY'] = SECRET_KEY

DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}

CORS_ORIGIN_WHITELIST = [
    "http://localhost:4200",
    "http://127.0.0.1:4200"
]

INSTALLED_APPS += ['rphc_commands']
