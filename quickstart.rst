===================================================================================
QUICKSTART
===================================================================================

After installing mantis as described in the installation description,
have a try at the following:

- Start with Mandiant_APT1_Report.xml: that goes relatively fast;
  Appendix_G_IOCs_Full.xml will take about 20 minutes or so to import::

       cd /home/mantis/ti/django_mantis
       python manage.py mantis_stix_import <path_to_stix_file> --settings=mantis.settings.local

  **ATTENTION**: The import of large files takes quite a bit of memory (probably there is a memory leak
  somewhere, which will be ironed out in a future release). Be sure to give the system/virtual machine
  you are running the import of ``Appendix_G_IOCs_Full.xml`` on a fair amount of memory (4 GB definitely
  works).


- Start the server (if the quickstart-script has not started it already for you)
  with::

       bash /home/ti/mantis/quickstart_files/install_scripts/90_start_services_ubuntu_13_10.sh
 
 - Browse to::   
   
        127.0.0.1:8000/mantis/View/InfoObject

  and start looking around:

  - Select a filter for ``stix.mitre.org:STIX_Package``
    in the filter box in the top-right corner. 

  - This will show you all ``STIX_Package``
    objects that are in the system (two, if you imported both ``Mandiant_APT1_Report.xml``
    and ``Appendix_G_IOC_Full.xml``). 

  - Click on one of the two objects and start
    exploring (have a look at the screenshots in the documentation for
    a quick guide through the application.)

  You can also have a look at the Django admin interface at::

        127.0.0.1:8000/admin



