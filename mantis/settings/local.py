from .base import *


#
# Settings that help with debugging
#


DEBUG = True

TEMPLATE_DEBUG = DEBUG

TEMPLATE_STRING_IF_INVALID = "INVALID EXPRESSION: '%s'"

#
# Add debug toolbar
#

MIDDLEWARE_CLASSES_list.append('debug_toolbar.middleware.DebugToolbarMiddleware')

MIDDLEWARE_CLASSES = tuple(MIDDLEWARE_CLASSES_list)

# Setting for debug toolbar

INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS = tuple(INSTALLED_APPS_list
                       + ['debug_toolbar']
                       #+ ['devel'] ## auto-create test root user on syncdb
                       + ['south'])

# Add loggers

STANDARD_CONSOLE_LOGLEVEL = 'INFO'

LOGGING['loggers']['dingos'] =  {
    'handlers': ['console'],
    'level': STANDARD_CONSOLE_LOGLEVEL,
    'propagate': True,
    }

LOGGING['loggers']['mantis'] =  {
    'handlers': ['console'],
    'level': STANDARD_CONSOLE_LOGLEVEL,
    'propagate': True,
    }


LOGGING['loggers']['mantis_openioc_importer'] =  {
    'handlers': ['console'],
    'level': STANDARD_CONSOLE_LOGLEVEL,
    'propagate': True,
    }

LOGGING['loggers']['mantis_stix_importer'] =  {
    'handlers': ['console'],
    'level': STANDARD_CONSOLE_LOGLEVEL,
    'propagate': True,
    }

LOGGING['loggers']['mantis_iodef_importer'] =  {
    'handlers': ['console'],
    'level': STANDARD_CONSOLE_LOGLEVEL,
    'propagate': True,
    }

LOGGING['loggers']['mantis_taxii'] =  {
    'handlers': ['console'],
    'level': STANDARD_CONSOLE_LOGLEVEL,
    'propagate': True,
    }



ADMINS = (
)

MANAGERS = ADMINS



DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/tmp/django-mantis_test.db',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }
