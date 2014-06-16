# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

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

                       # Include the authoring apps and the authoring base (dingos_authoring)
                       url(r'^mantis/authoring/', include('dingos_authoring.urls')),
                       url(r'^mantis/authoring/', include('mantis_authoring.urls')),


                       # Uncomment below to include URLs of MITRE's Yeti PoC app
                       #url(r'^taxii/', include('yeti.urls')),

                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# We have to import menus.py somewhere after the URLs have been configured.
# So, for now, we do it here. We used to do it in models.py, but for
# some reason (probably a change in django proper), this stopped working.



import menus
 
