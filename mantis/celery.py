from __future__ import absolute_import

import os

from celery import Celery

from django.conf import settings

# set the default Django settings module for the 'celery' program.

if not settings.configured:
    settings.configure()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mantis.settings.local_psql')

app = Celery('mantis')


app.config_from_object('django.conf:settings')

app.conf.update(
    CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
)



app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
