============
Installation
============

.. contents::

-------------------
Manual installation
-------------------

The installation instructions below have been tested on an out-of-the-box
installation of  `Ubuntu Desktop 12.04 LTS`_
(the Desktop rather than the Server version has been used, since the majority
of installs are likely to be for testing and developing, where having a full
working environment and X-server installed comes in handy.) If you are using
a different *nix flavor, you have to find the corresponding installation
packages used with ``apt-get`` below -- the installation steps
carried out with ``pip``, however, will be exactly the same.

*Attention*: If you are setting up a virtual machine, make sure to give
it at least 3GB of memory if you want to import really large XML
structures such as MITRE's STIX conversion of the 
Mandiant APT-1 report (http://stix.mitre.org/downloads/APT1-STIX.zip) -- 
importing large files currently takes a lot of memory -- there
seems to be a memory leak which we still have to track down.


#. Make sure that you have the required
   dependencies on OS level for building the XML-related packages. For
   example, on an Ubuntu system, execute the following commands::

     $ apt-get install libxml2 libxml2-dev python-dev libxslt1-dev

   Also, while you are at it, install git, if you do not have it already::
  
     $ apt-get install git

   If you are behind a proxy, you can configure a proxy for
   ``apt-get`` by putting a file ``95proxy`` into ``/etc/apt/apt.conf.d``
   that has the following contents::

      Acquire::http::proxy "<proxy_url>";
      Acquire::ftp::proxy "<proxy_url>";
      Acquire::https::proxy "<proxy_url>";



#. It is recommended to use a virtual python environment.

   - Make sure that ``virtualenv`` and ``pip`` are installed::

        $ apt-get install python-virtualenv python-pip

   - Create a virtual environment::

        $ virtualenv <path_for_storing_environments>/mantis
        $ source <path_for_storing_environments>/mantis/bin/activate

     Now the virtual environment is activated -- you should see a changed 
     prompt that is prefixed with ``(mantis)``

#. Install the ``libxml2-python`` bindings

   Unfortunately, the process of getting ``libxml2-python`` installed using ``pip`` varies from
   OS to OS, because there is no proper library package available.

   * For Ubuntu 12.04 do the following:

     Use pip to install directly from an ftp source::

          (mantis)$ pip install ftp://xmlsoft.org/libxml2/python/libxml2-python-2.6.21.tar.gz 

     If you are behind a proxy, you can either provide ``pip`` with the proxy information with the
     commandline argument ``--proxy  <proxy_url>`` or use the ``http_proxy`` environment variable --
     do not do both, because this confuses ``pip``.
     

     If the download does not work via pip, download the file with your browser, and install from file
     with ``pip install <filename>``.

   * For Ubuntu 13.10, do the following:

     * Downloadand unpack the ``libxml2`` sources::

           (mantis)$ wget http://xmlsoft.org/sources/libxml2-2.9.1.tar.gz"
           (mantis)$ tar -zxvf libxml2-2.9.1.tar.gz

       If you are behind a proxy, append ``-e use_proxy=yes -e http_proxy=<proxy_url>`` after the
       URL when calling ``wget``.

     * Install via ``pip``::

           (mantis)$ pip install libxml2-2.9.1/python

       If you are behind a proxy, you can either provide ``pip`` with the proxy information with the
       commandline argument ``--proxy  <proxy_url>`` or use the ``http_proxy`` environment variable --
       do not do both, because this confuses ``pip``.


#. Go to a location where you want to have the Django Mantis files and check out the git repository::

      (mantis)$ git clone https://github.com/siemens/django-mantis.git
      
   If you are behind a proxy, you can configure a proxy for ``git`` via the following::

       (mantis)$ git config --global http.proxy <proxy_url>

#. Change into the ``django-mantis`` directory and do::

      (mantis)$ pip install -r requirements/local.txt
      (mantis)$ pip install django-simple-menu>=1.0.6

   (For some reason, ``django-simple-menu`` cannot be installed before Django itself has not been
   installed completely).


#. Your are now all set for running MANTIS on top of an SQLite database. If that is what you want to do,
   have a look at :doc:`quickstart`. 

#. For running MANTIS on top of Postgresql (which is
   recommended), you need to install and prepare Postgresql:

   - Install it::
 
          $ apt-get install postgresql
          $ apt-get install postgresql-server-dev-9.1 

   - Install the Python module for working with postgresql::

          (mantis)$ pip install psycopg2

   - In ``/etc/postgresql/9.1/main/postgresql.conf`` set ``ssl = False``
 
   - (Re)start the server::
         
          /etc/init.d/postgresql start
 
   - Create password for ``postgresql``: as root user, do::
 
       passwd postgres
 
   - Give the postgresql user a database password; As user ``postgres`` do::
 
         su postgres
         psql
         \password postgres;
 
   - Prepare database: 
   
     - As user postgresql do::
 
          createuser -P mantis;
 
       and do the following:
 
       - give it password ``mantis``
       - do not make it super user
       - allow it to create databases (required for running python unit tests). If you forgot about this step here, you can
         later run (``ALTER USER mantis CREATEDB;``) on the database prompt to achieve the same.
       - do not allow it to create new roles
 
 
   - In database, do::
 
       CREATE DATABASE django OWNER mantis ENCODING 'UTF-8';
 
   - In ``/etc/postgresql/9.1/main/pg_hba.conf`` enter after the line for the postgres user::
 
        # TYPE  DATABASE        USER            ADDRESS                 METHOD
 
        local [tab] django [tab] mantis [tab][tab]  md5

#. Continue with the  :doc:`quickstart`. 



------------------------------------------
(Semi-)automated installation with Vagrant
------------------------------------------

`Vagrant`_ allows automated provisioning of virtual machines with
preconfigured packages, configuration settings, etc. 

(Development of Vagrant deployment scripts for Mantis is an ongoing
effort. Scripts and documentation will be published as they become
ready.)



.. _Ubuntu Desktop 12.04 LTS: http://www.ubuntu.com/download/desktop

.. _Vagrant: http://www.vagrantup.com/
