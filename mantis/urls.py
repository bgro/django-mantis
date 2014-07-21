# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static


# The following import seems to be necessary to have somewhere where
# it is carried out at an early stage;
# otherwise the celery tasks in the apps are not initialized properly.

from . import celery

from .views import MessagingTestView, HomeView

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

                       # specialized views for STIX/CybOX objecte
                       url(r'^mantis/', include('mantis_stix_importer.urls')),

                       # Include the authoring apps and the authoring base (dingos_authoring)
                       url(r'^mantis/Authoring/', include('dingos_authoring.urls')),
                       url(r'^mantis/Authoring/', include('mantis_authoring.urls')),


                       # Include some test views

                       url(r'^mantis/Test/Messaging', MessagingTestView.as_view()),

                       # An empty home view
                       url(r'^mantis/?$', HomeView.as_view()),

                       # Uncomment below to include URLs of MITRE's Yeti PoC app
                       #url(r'^taxii/', include('yeti.urls')),



                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.USE_DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )

# We have to import menus.py somewhere after the URLs have been configured.
# So, for now, we do it here. We used to do it in models.py, but for
# some reason (probably a change in django proper), this stopped working.



import menus
 
