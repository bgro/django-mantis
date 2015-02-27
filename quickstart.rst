===================================================================================
QUICKSTART
===================================================================================

After installing mantis as described in the installation description,
have a try at the following:
 
 - Browse to::   
   
        127.0.0.1:8000/mantis

   and log in with user ``admin`` and password ``admin``

 - Use the menu bar at the top and select the first saved search
   that filters for STIX packages. This will show you all ``STIX_Package``
   objects that are in the system 

 - Click on one of the displayed packages and start exploring (have a look
   at the screenshots in the documentation for a quick guide through
   the application.)

 - You can also have a look at the Django admin interface at::

        127.0.0.1:8000/admin

 - If you want to create a STIX report, you first have to
   add your user to an "authoring group":

   - Go to the admin interface (either via the top-right menu
     or by browsing to ``127.0.0.1:8000/admin``)

   - Create a Django group (``http://127.0.0.1:8000/admin/auth/group/``), 
     that will be used as authoring group. For example, name it ``my_organization``
     and save the group.
   - Edit your user (``http://127.0.0.1:8000/admin/auth/user/``)
     and add it to the created group.
   - Create an identifier namespace (``http://127.0.0.1:8000/admin/dingos/identifiernamespace/``), e.g.,
     ``my_organization.com``; you can upload an image
     for that namespace that will later be used when
     displaying the namespace to the user (e.g., in an
     object overview).

   - Associate the created namespace with the authoring group by
     creating a mapping between the two
     (``http://127.0.0.1:8000/admin/dingos_authoring/groupnamespacemap/``):
     by chosing the created namespace as default namespace, STIX
     reports authored via the GUI will be placed in that particular
     namespace. Adding further namespaces in the mapping as
     "allowed namespaces" will enable the user to import STIX XML files
     in one ore more of the allowed namespaces via the GUI.

   Now return from the admin interface to the Mantis pages and chose
   "New Report" in the Menu "Authoring" and wait for the authoring
   GUI to load. Once it is loaded, you can do the following:

   - create indicators on the indicator tab
   - create observables on the observables tab
   - add relationships between observables on the relationship tab
   - associate observables with indicators by pulling observables
     from the bottom right into one of the indicators on the
     central pane on the STIX package tab.
  
   Once you have authored a report, you can import it via
   the "Import to MANTIS" button. Returning to the overview
   of reports via the "authoring" menu should show you
   an entry for the created report and a little magnifying
   glass next to the word 'Imported' -- pressing on the
   magnifying glass will take you to the top-level object
   (the STIX package) resulting from the import.






