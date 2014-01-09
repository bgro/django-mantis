MANTIS Application Layout
=========================

.. contents::

Overview of the directory layout
--------------------------------

The layout of the DINGOS Django application is as follows::

      .
      ├── mantis
      │   ├── apps
      │   ├── assets
      │   ├── blobs
      │   ├── menus.py
      │   ├── models.py
      │   ├── settings
      │   │   ├── base.py
      │   │   ├── local_psql.py
      │   │   ├── local.py
      │   │   ├── production.py
      │   │   └── testing.py
      │   ├── static
      │   ├── templates
      │   │   ├── 404.html
      │   │   ├── 500.html
      │   │   ├── base.html
      │   │   ├── dingos
      │   │   │   └── grappelli
      │   │   │       └── base.html
      │   │   └── mantis
      │   │       └── grappelli
      │   ├── urls.py
      │   └── wsgi.py

