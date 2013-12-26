=========================================================
The MANTIS Cyber Threat Intelligence Management Framework
=========================================================

Architecture
------------

The MANTIS (Model-based Analysis of Threat Intelligence Sources) Framework consists
of several `Django`_ Apps that, in combination, support the management
of cyber threat intelligence expressed in standards such as `STIX`_, `CybOX`_,
`OpenIOC`_, `IODEF (RFC 5070)`_, etc.

The heavy lifting is done in the following Django Apps:

- `django-dingos`_
- `django-mantis-core`_
- `django-mantis-stix-importer`_
- `django-mantis-openioc-importer`_
- `django-mantis-iodef-importer`_
-  django-mantis-taxii (under development)


This project ``django-mantis`` provides a template Django Project that shows how these Django Apps can
be used as basis for your own MANTIS-based Cyber-Threat Intelligence Management system.


Documentation
-------------

The full documentation is at http://django-mantis.readthedocs.org.

Acknowledgments
---------------


The basic layout for this Django project with extremly useful base settings and very sensible directory layout
 was generated with Audrey Roy's excellent `Cookiecutter`_ and Marco Fucci's `cookiecutter-simple-django`_ template.


.. _Cookiecutter: https://github.com/audreyr/cookiecutter


.. _cookiecutter-simple-django: https://github.com/marcofucci/cookiecutter-simple-django



.. _Django: https://www.djangoproject.com/
.. _STIX: http://stix.mitre.org/
.. _CybOX: http://cybox.mitre.org/
.. _OpenIOC: http://www.openioc.org/
.. _IODEF (RFC 5070): http://www.ietf.org/rfc/rfc5070.txt

.. _django-dingos: https://github.com/siemens/django-dingos/blob/master/docs/what_dingos_is_all_about.rst
.. _django-mantis-core: https://github.com/siemens/django-mantis-core
.. _django-mantis-stix-importer: https://github.com/siemens/django-mantis-stix-importer
.. _django-mantis-openioc-importer: https://github.com/siemens/django-mantis-openioc-importer
.. _django-mantis-iodef-importer: https://github.com/siemens/django-mantis-iodef-importer
