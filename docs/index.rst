..  documentation master file, created by
   sphinx-quickstart on Sun Feb 17 11:46:20 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

The MANTIS Cyber-Intelligence Management Framework
==================================================

The MANTIS (Model-based Analysis of Threat Intelligence Sources) Framework consists
of several `Django`_ Apps that, in combination, support the management
of cyber threat intelligence expressed in standards such as `STIX`_, `CybOX`_,
`OpenIOC`_, `IODEF (RFC 5070)`_, etc.

Important resources:

* Access to the Mantis source code for installation:

  * Either via ``git clone`` from the   `Mantis Github Repository`_ (recommended)::

       git clone https://github.com/siemens/django-mantis.git

  * Or via download as ``zip`` package from https://github.com/siemens/django-mantis/archive/master.zip
   
* There is a mailing list for dicussions, questions, etc.: 
  
  * Subscribe to the mailing list by sending a mail to ``Mantis-ti-discussion-join@lists.trusted-introducer.org``.

  * The archives of the mailing list are available via `Nabble`_.

* All issues regarding Mantis and its components are tracked
  on the `Mantis Issue Tracker`_.

* Documentation:

  .. toctree::
     :maxdepth: 1

     architecture
     screenshots
     what_mantis_is
     installation
     quickstart
     mantis_developers_guide
     contributing


.. _Nabble: http://mantis-threat-intelligence-management-framework-discussion-list.57317.x6.nabble.com/
.. _Mantis Github Repository: https://github.com/siemens/django-mantis
.. _Mantis Issue Tracker: https://github.com/siemens/django-mantis/issues?state=open

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
