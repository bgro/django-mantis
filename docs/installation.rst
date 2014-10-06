============
Installation
============

.. contents::

-------------------
Manual installation
-------------------

The installation instructions below have been tested on an out-of-the-box
installation of  `Ubuntu Desktop 13.10`_
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
(*Note*: this may have to do with a known memory leak of Django that
occurs when ``DEBUG=TRUE`` is set).

#. If you are behind a proxy, use the graphical user interface
   for setting the proxy (``System Settings > Network``)

#. Make sure that you have ``git`` installed::

       sudo apt-get install git

   If you are behind a proxy, configure to use the proxy::

      git config --global http.proxy $HTTP_PROXY
      git config --global https.proxy $HTTP_PROXY


#. If you have not already done so during installation of the
   operating system, create a user ``mantis``::

      useradd mantis

   and log in as this user.

#. In  ``/home/mantis``, create a folder ``ti``::

       mkdir /home/mantis/ti 
       cd /home/mantis/ti 

#. Clone the ``django-mantis`` repository from github and change to
   the development branch::

      git clone https://github.com/siemens/django-mantis.git
      cd django-mantis
      git checkout development
      cd ..      

#. Copy the installation files to top-level of the ``ti`` directory:: 

     cp django-mantis/quickstart_files/install_scripts/*.sh /home/mantis/ti

     
#. Install the required packages::
     
     cd /home/mantis/ti
     bash 10_install_packages_ubuntu_13_10.sh

#. Configure postgresql::

     cd /home/mantis/ti
     sudo -i -u postgres
     bash /home/mantis/ti/20_configure_psql_ubuntu_13_10.sh
     exit
     
#. Create development environment::

     cd /home/mantis/ti
     bash 30_create_dev_env_ubuntu_13_10.sh
     



.. _Ubuntu Desktop 13.10: http://releases.ubuntu.com/13.10/

