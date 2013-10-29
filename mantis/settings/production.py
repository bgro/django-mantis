from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
)

MANAGERS = ADMINS


get_env_variable('DJANGO_SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'mantis',
        'PASSWORD': get_env_variable('DJANGO_DB_PASSWORD'),
        'HOST': '',
        'PORT': '',
    }
}
