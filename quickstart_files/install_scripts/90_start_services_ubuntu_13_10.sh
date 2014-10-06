sudo /etc/init.d/celeryd start
cd /home/mantis/ti/django-mantis
source /home/mantis/.virtualenvs/mantis_dev/bin/activate
python manage.py runserver 0.0.0.0.:8000 --insecure --settings=mantis.settings.local_psql
