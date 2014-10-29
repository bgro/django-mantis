# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.http import HttpResponseRedirect


from dingos_authoring import views as dingos_authoring_views

# The following import seems to be necessary to have somewhere where
# it is carried out at an early stage;
# otherwise the celery tasks in the apps are not initialized properly.

from . import celery

from .views import MessagingTestView, HomeView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns(
    '',

    # Default entry point
    url(r'^$', lambda x: HttpResponseRedirect('/mantis/dashboard'), name="url.mantis.startpage" ),


    # Grappeli documentation
    (r'^grappelli/', include('grappelli.urls')),


    # Admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


    # Admin Interface
    url(r'^admin/', include(admin.site.urls)),


    # MANTIS Urls -- currently, we just take the stuff from DINGOS
    # but that is likely to change soon
    url(r'^mantis/', include('dingos.urls')),


    # Specialized views for STIX/CybOX objects
    url(r'^mantis/', include('mantis_stix_importer.urls')),


    # Include the authoring app and the authoring base (dingos_authoring)
    url(r'^mantis/Authoring/', include('dingos_authoring.urls')),
    url(r'^mantis/Authoring/', include('mantis_authoring.urls')),

    # Make xml source saved during import accessible

    #url(r'^mantis/View/InfoObject/(?P<pk>\d*)/xml/source$',
    #    dingos_authoring_views.ImportedXMLView.as_view(),
    #    name= "url.dingos_authoring.view.infoobject.xml.source"),



    # Include the Siemens Dashboard app
    url(r'^mantis/dashboard/', include('mantis_dashboard.urls', namespace='mantis_dashboard')),


    # Our API
    url(r'', include('mantis_api.urls')),
    url(r'', include('mantis_api_siemens.urls')),


    # OAuth2 Provider URLs
    url(r'^oauth2/', include('provider.oauth2.urls', namespace = 'oauth2')),


    # Uncomment below to include URLs of MITRE's Yeti PoC app
    #url(r'^taxii/', include('yeti.urls')),


    # Debug toolbar URL mapping
    #url(r'^__debug__/', include(debug_toolbar.urls)),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.USE_DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
