if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi
#set postmaster path to virtual environment
echo PATH=\'/home/mantis/.virtualenv/mantis_dev/bin\' >> /etc/postgresql/9.1/main
/etc/init.d/postgresql restart

/etc/init.d/celeryd start
cd /home/mantis/ti/django-mantis
source /home/mantis/.virtualenvs/mantis_dev/bin/activate
python manage.py runserver 0.0.0.0:8000 --settings=mantis.settings.local_psql
