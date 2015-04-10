============
Installation
============

.. contents::

-------------------
Manual installation
-------------------

*Note*: What is described below is a quickstart installation, setting
default passwords both for the database and the Django system, etc.

The installation instructions below have been tested on an out-of-the-box
installation of  `Ubuntu Desktop 14.04`_
(the Desktop rather than the Server version has been used, since the majority
of installs are likely to be for testing and developing, where having a full
working environment and X-server installed comes in handy.) If you are using
a different *nix flavor, you have to find the corresponding installation
packages used with ``apt-get`` below -- the installation steps
carried out with ``pip``, however, will be exactly the same.

*Attention*: When Django's debugging is switched on (``DEBUG=TRUE``),
there is a memory leak. so, if you are setting up a virtual machine, and want
to carry out imports of large files with Django's debug 
setting switched on, make sure to give
it at least 3GB of memory.

#. If you are behind a proxy, use the graphical user interface
   for setting the proxy (``System Settings > Network``):
   set the proxy and apply it system-wide.

   Be sure to open a new terminal for the following steps
   in order to propagate the proxy information also into
   the terminal's environment.

#. Make sure that you have ``git`` installed::

       sudo apt-get install git

   If you are behind a proxy, configure to use the proxy::

      git config --global http.proxy $HTTP_PROXY
      git config --global https.proxy $HTTP_PROXY


#. If you have not already done so during installation of the
   operating system, create a user ``mantis``::

      sudo useradd mantis

   and log in as this user.

#. In  ``/home/mantis``, create a folder ``ti``::

       mkdir /home/mantis/ti 
       cd /home/mantis/ti 

#. Clone the ``django-mantis`` repository from github and change to
   the development branch::

      git clone https://github.com/siemens/django-mantis.git
      cd django-mantis
      git checkout development_0_4_0
      cd ..      

#. Copy the installation files to top-level of the ``ti`` directory:: 

     cp django-mantis/quickstart_files/install_scripts/* /home/mantis/ti

     
#. Install the required packages::
     
     cd /home/mantis/ti
     sudo bash 10_install_packages_ubuntu_14_04.sh

#. Configure postgresql::

      cd /home/mantis/ti
      sudo bash /home/mantis/ti/20_configure_psql_ubuntu_14_04.sh
     
#. Create development environment::

      cd /home/mantis/ti
      bash 30_create_dev_env_ubuntu_14_04.sh

#. Start the services (Celery and Django)::

      cd /home/mantis/ti
      bash 70_start_services_ubuntu_13_10.sh

   Now you can log into the system at  ``127.0.0.1:8000/mantis``
   using the user ``admin`` with password ``admin``.

#. (Optional): Pull some sample data into the system::

      cd /home/mantis/ti
      bash 80_import_sample_data_ubuntu_13_10.sh

   (Use a different shell or interrupt the server while importing;
   the celery service will still run in the background and make
   sure that basic indicators found in the imported data are
   transfered into the Mantis Actionables application.)


.. _Ubuntu Desktop 14.04: http://releases.ubuntu.com/14.04/

