import sys, os, re, tempfile
from os.path import join, abspath, dirname
from django.core.exceptions import ImproperlyConfigured

from mantis_stix_importer import STIX_OBJECTTYPE_ICON_MAPPING, STIX_OBJECTTYPE_VIEW_MAPPING, STIX_POSTPROCESSOR_REGISTRY


def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s env variable" % var_name
        raise ImproperlyConfigured(error_msg)




# PATH vars

here = lambda *x: join(abspath(dirname(__file__)), *x)
PROJECT_ROOT = here("..")
root = lambda *x: join(abspath(PROJECT_ROOT), *x)

sys.path.insert(0, root('apps'))


USE_DEBUG_TOOLBAR = False



DEBUG_TOOLBAR_CONFIG = {'SHOW_TOOLBAR_CALLBACK': "mantis.settings.setting_utils.mantis_show_toolbar"}

DEBUG_TOOLBAR_PATCH_SETTINGS = False

DEBUG_TOOLBAR_IPS = ["127.0.0.1"]


# Make this unique, and don't share it with anybody.
SECRET_KEY = "CHANGE THIS"

# Configuration for apps used in the framework

## Grappelli

# The title of the menu bar

GRAPPELLI_ADMIN_TITLE = "MANTIS Cyber Threat Info Management"

## DINGOS

DINGOS = {
           # The OWN_ORGANIZATION_ID_NAMESPACE is used as default namespace for object identifiers
           # if no namespace is provided
          'OWN_ORGANIZATION_ID_NAMESPACE': 'own.organization.com',

           # We do not want to write really large values to the FactValue table:
           # with the current postgresql config, large values make trouble,
           # because we enforce uniqueness on the FactValue table, and that
           # requires indexing, which fails with the default config.
           # This may be overcome by tweaking indexing in Postgresql. Until
           # then, use a maximum size limit no larger than 2048.
           'DINGOS_MAX_VALUE_SIZE_WRITTEN_TO_VALUE_TABLE' : 2048,
           # The possible destinations for large values are:
           # - DINGOS_BLOB_TABLE: a dedicated table for large values
           # - DINGOS_FILE_SYSTEM: the file system
           # - DINGOS_VALUES_TABLE: write to the values table anyways
          'LARGE_VALUE_DESTINATION' : 'DINGOS_BLOB_TABLE',
           # - The BLOB_ROOT specifies the location on the filesystem to which large values are written
           'BLOB_ROOT' : root('blobs'),

           # Later versions of DINGOS may support other CSS frameworks. Until then, the
           # template family must remain 'grappelli'
          'TEMPLATE_FAMILY' : 'grappelli',

          # Below, we define sample saved searches. These make only sense, if the
          # the import commands for the default naming schemas have been carried out in
          # exactly the same order as specified in the quickstart(_psql).sh scripts --
          # otherwise, the identifiers specified in the searches (here '72' for InfoObjectType
          # STIX_Package) will not work.
          'DINGOS_DEFAULT_SAVED_SEARCHES' : {
              'dingos' : [
                  { 'priority' : "0",
                    'title' : 'Filter for STIX Packages',
                    'view' : 'url.dingos.list.infoobject.generic',
                    'parameter' : 'iobject_type=72',
                    }
              ],
              },
          'DINGOS_DEFAULT_USER_PREFS' : {
              'dingos' : { 'widgets' :
                               {'embedded_in_objects' :
                                    {'lines' : {'@description': """Max. number of objects displayed in
                                                        widget listing the objects in which the
                                                        current object is embedded.""",
                                                '_value' : '5'}
                                    } ,
                                },
                           'view' :
                               {'pagination':
                                    {'lines' : {'@description': """Max. number of lines displayed in
                                                    paginated views.""",
                                                '_value' : '20'},
                                     },
                                'orientation' : {'@description': """Layout orientation. Possible values are 'auto', 'vertical' and
                                                          'horizontal'.""",
                                                 '_value' : 'auto'}
                               }

              }
},

    # We define the mapping of object types to images for the graph view:
    'OBJECTTYPE_ICON_MAPPING': STIX_OBJECTTYPE_ICON_MAPPING,
    # We define the mapping of object types to specialized views
    'OBJECTTYPE_VIEW_MAPPING': STIX_OBJECTTYPE_VIEW_MAPPING,
    'SEARCH_POSTPROCESSOR_REGISTRY' : STIX_POSTPROCESSOR_REGISTRY,
}


# DINGOS authoring specific configuration
DINGOS_AUTHORING = {
   'IMPORTER_REGISTRY' : ( (re.compile("http://stix.mitre.org.*"), "mantis_stix_importer.importer","STIX_Import"),
                           (re.compile("http://cybox.mitre.org.*"), "mantis_stix_importer.importer","STIX_Import"),
                           (re.compile("http://schemas.mandiant.com/2010/ioc"), "mantis_openioc_importer.importer","OpenIOC_Import") ),
   'DATA_FILESYSTEM_ROOT' : root('authoring', 'imports')
}

# MANTIS authoring specific configuration
MANTIS_AUTHORING = {
    # Path to a directory where uploaded files are temporarily stored for analysis (content detection)
    'FILE_CACHE_PATH': join(tempfile.gettempdir(), 'mantis_authoring')
}
if not os.path.isdir(MANTIS_AUTHORING['FILE_CACHE_PATH']):
    os.mkdir(MANTIS_AUTHORING['FILE_CACHE_PATH'])



LOGIN_REDIRECT_URL = "/mantis"

LOGIN_URL = "/mantis/login"

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = ()

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'mantis',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Berlin'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = root('assets', 'uploads')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = root('static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    root('assets'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


MIDDLEWARE_CLASSES_list = []



MIDDLEWARE_CLASSES_list += MIDDLEWARE_CLASSES_list + [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if USE_DEBUG_TOOLBAR:
    MIDDLEWARE_CLASSES_list.append('debug_toolbar.middleware.DebugToolbarMiddleware')
    INTERNAL_IPS=DEBUG_TOOLBAR_IPS


MIDDLEWARE_CLASSES = tuple(MIDDLEWARE_CLASSES_list)


# Add context processors
# (without these, templates have no access to request etc.

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

ROOT_URLCONF = 'mantis.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'mantis.wsgi.application'

TEMPLATE_DIRS = (
    root('templates'),
)

INSTALLED_APPS_list = [
    'debug_toolbar',
    'grappelli',
    'djcelery',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    # We use django-simplemenu for displaying menu structures
    'menu',
    # Below, the MANTIS components are installed
    'mantis',
    'dingos',
    'dingos_authoring',
    'mantis_core',
    'mantis_openioc_importer',
    'mantis_stix_importer',
    'mantis_iodef_importer',
    'mantis_authoring',

    # Include the Dashboard!
    #'mantis_dashboard',

    # Include the django-oauth2-provider
    'provider',
    'provider.oauth2',

    # Include the Mantis API
    #'mantis_api',

    #
    # Uncomment below to include TAXII SERVICES and YETI from MITRE's
    # TAXII PoC implementation YETI
    #  (you must make these available to Django, e.g. by symlinking
    #   the app directories into the 'django-mantis' directory;).
    #   in order to use the taxii services, you must also
    #   append the url.py configuration
    #
    #'taxii_services',
    #'yeti',
]

#if USE_DEBUG_TOOLBAR:
#    INSTALLED_APPS_list.append('debug_toolbar')

INSTALLED_APPS = tuple(INSTALLED_APPS_list)

PROJECT_APPS = ()

INSTALLED_APPS += PROJECT_APPS


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}



# Celery configuration

CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'

BROKER_URL = 'amqp://guest:guest@localhost:5672//'




