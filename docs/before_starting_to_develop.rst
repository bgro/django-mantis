Before starting to develop
==========================


Read up on techniques and styles used in MANTIS
-----------------------------------------------

MANTIS profitted a lot from the advice provided in `Two Scoops of Django`_.

Unless you are an absolute Django expert (and maybe even then), please
read Daniel Greenfield's and Audrey Roy's excellent `Two Scoops of Django`_.
Even though it provides best practices for Django 1.5, most of its
advice is also valid for Django 1.6, and likely to be very relevant
for quite a few minor revisions to come.


Understand how django-dingos works
----------------------------------

The heart of MANTIS is the `django-dingos`_ Django application.
Most aspects of modifying/adding to MANTIS will require
a sound understanding of how `django-dingos` works.
Please refer to the `Django DINGOS developers' guide`_


Find the right place to modify/add to: Keep django-dingos generic
-----------------------------------------------------------------

Although DINGOS is likely to be used mainly in the context of the
Django MANTIS Cyber Threat Intelligence Management application,
DINGOS shold stay a /generic/ application for managing
structured information. So whenever you find yourself
adding/modifying stuff in DINGOS that is specific to
cyber threat intelligence management, the STIX, CybOX standards,
etc., **DINGOS is the wrong place to modify/add to**. The same goes
for customizations that are particular to your instance
of running MANTIS.

Please consider the following places for development instead:

* If you want to add Python code that is particular to cyber threat
  management, consider adding this in `django-mantis-core`_

* If you want to add Python code that is particular to a certain
  standard, consider adding it to the respective importer module,
  e.g., `django-mantis-stix-importer`_ or similar

* If you want to make modifications to a DINGOS template that
  is required for your local instance of MANTIS (or whatever
  framework is using DINGOS), the right way is probably
  to override one of the DINGOS base templates. Have a look
  at how `django-mantis`_ overrides the
  ``templates/dingos/grappelli/base.html`` template;
  see also the `Django documentation on overriding templates`_.

* If you want to change the url paths of DINGOS views,
  do this in the ``url.py`` of your instance rather
  than ``dingos/url.py``.








.. _Two Scoops of Django: https://django.2scoops.org/
.. _django-mantis-core: https://github.com/siemens/django-mantis-core
.. _django-mantis-stix-importer: https://github.com/siemens/django-mantis-stix-importer
.. _django-mantis: https://github.com/siemens/django-mantis
.. _Django documentation on overriding templates: https://docs.djangoproject.com/en/1.6/intro/tutorial02/#ref-customizing-your-projects-templates
.. _django-dingos: https://github.com/siemens/django-dingos
.. _Django DINGOS developers' guide: http://django-dingos.readthedocs.org/en/latest/developers_guide.html
