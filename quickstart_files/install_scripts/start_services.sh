sudo /etc/init.d/celeryd start
cd /home/mantis/ti/django-mantis
python manage.py runserver 0.0.0.0.:8000 --settings=mantis.settings.local_psql