===================
MANTIS Architecture
===================

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

.. figure:: images/mantis_architecture.PNG
   :align: center
   :scale: 50%

   MANTIS architecture


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
