Setting up a development environment
====================================

#. Refer to :doc:`contributing` (section "Getting Started") for information of how to fork a repository, clone it,
   and install it for development purposes.

#. Chose a development environment of your liking. Here is how you can setup 
   `PyCharm`_ Professional Edition in support of development for Django:
    * Start up PyCharm and enter your license information.
    * Before opening a project/folder, go to ``Configure -> Settings`` and adjust the following:
      - Use the search box in the settings dialog to find the place where you can configure the proxy settings:
      - Configure the python environment under "Project Interpreter" -> "Python Interpreters"
        Click on the "+", then on "Local..."
	Select ``<path_to_your_environment>/bin/python``, and click "Ok"
      - Click on "Ok" to close the settings window.
    * Open the project folder: select "Open Directory" and choose your source directories 
    
    * Before being able to run the django-mantis project, you have to adjust the "Run/Debug Confgurations" (wait for the indexer to finish...)
      - In the menubar, click on "Run" -> "Edit Configurations"
      - Select the "django-mantis" in the displayed tree on the left
      - In the right pane, add the following to the "Additional options:" ``--settings=mantis.settings.local_psql`` or ``--settings=mantis.settings.local``  

    * You should now be able to run the django server by clicking the play button.

.. _PyCharm: http://www.jetbrains.com/pycharm/
