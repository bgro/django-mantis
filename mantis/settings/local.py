from .base import *


#
# Settings that help with debugging
#


DEBUG = True

TEMPLATE_DEBUG = DEBUG

TEMPLATE_STRING_IF_INVALID = "INVALID EXPRESSION: '%s'"

#
# To add the django-debug-toolbar (an essential tool for own development)
# try uncommenting the lines below.
# If you run into an issue with this (error messages 'NoReverseMatch: u'djdt' is not a registered namespace'),
# you can instead try the explicit setup of the debug toolbar as described at
# http://django-debug-toolbar.readthedocs.org/en/1.0/installation.html#explicit-setup
#

#MIDDLEWARE_CLASSES_list.append('debug_toolbar.middleware.DebugToolbarMiddleware')
#INSTALLED_APPS_list.append('debug_toolbar')
#INTERNAL_IPS = ('127.0.0.1',)



# Configure middleware classes and installed apps


MIDDLEWARE_CLASSES = tuple(MIDDLEWARE_CLASSES_list)

INSTALLED_APPS = tuple(INSTALLED_APPS_list
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
