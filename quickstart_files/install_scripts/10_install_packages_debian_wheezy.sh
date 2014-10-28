#!/bin/bash
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi
echo "Installing required packages"
apt-get install libxml2 libxml2-dev python-dev libxslt1-dev python-virtualenv python-pip postgresql postgresql-server-dev-9.1 rabbitmq-server libldap2-dev plpython-9.1
echo "Copying celery scripts"
cp django-mantis/quickstart_files/celery/celeryd_config /etc/default/celeryd
cp django-mantis/quickstart_files/celery/celeryd_initscript /etc/init.d/celeryd
chmod uoa+x /etc/init.d/celeryd