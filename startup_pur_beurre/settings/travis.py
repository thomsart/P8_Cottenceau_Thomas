from . import *

SECRET_KEY = 'KEY'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pur_beurre_db',
        'USER': 'thoms',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

