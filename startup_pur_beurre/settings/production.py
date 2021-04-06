from . import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from django.urls import path


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

sentry_sdk.init(
    dsn="https://ffa08fcca6f7465689fad60dab6448da@o565870.ingest.sentry.io/5707926",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=0.7,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('sentry-debug/', trigger_error),
    # ...
]
INSTALLED_APPS += [
            'raven.contrib.django.raven_compat',
            ]


RAVEN_CONFIG = {
            'dsn': 'https://somethingverylong@sentry.io/216272', # caution replace by your own!!
                # If you are using git, you can also automatically configure the
                    # release based on the git info.
                        'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
                        }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'INFO', # WARNING by default. Change this to capture more than warnings.
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
            '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'INFO', # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
