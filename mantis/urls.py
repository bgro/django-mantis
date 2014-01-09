# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import extdirect.django as extdirect
extdirect.autodiscover()

urlpatterns = patterns('',
                       # Grappeli documentation
                       (r'^grappelli/', include('grappelli.urls')),

                       # Admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Admin Interface
                       url(r'^admin/', include(admin.site.urls)),

                       # MANTIS Urls -- currently, we just take the stuff from DINGOS
                       # but that is likely to change soon

                       url(r'^mantis/', include('dingos.urls')),

                       # Uncomment below to include URLs of MITRE's Yeti PoC app
                       url(r'^taxii/', include('yeti.urls')),

                       url(r'^ext/', include('dingos_extjs.urls')),
                       url(r'^extdirect/', include('extdirect.django.urls'))

                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

