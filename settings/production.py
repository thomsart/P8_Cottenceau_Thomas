from . import *

SECRET_KEY = 'dd65h51h61rlbs<dsrr51hdtdf16171sf15y6jf611nf'
DEBUG = False
ALLOWED_HOSTS = ['178.62.70.233']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pur_beurre_db',
        'USER': 'thomas',
        'PASSWORD': 'metalspirit77+',
        'HOST': '',
        'PORT': '5432',
    }
}
