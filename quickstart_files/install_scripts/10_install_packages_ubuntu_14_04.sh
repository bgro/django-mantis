sudo touch  /etc/apt/sources.list.d/pgdg.list
echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" | sudo tee -a /etc/apt/sources.list.d/pgdg.list
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update

cd /home/mantis/ti
echo "Running apt-get"
sudo apt-get install libxml2 libxml2-dev python-dev libxslt1-dev python-virtualenv python-pip postgresql postgresql-server-dev-9.4 rabbitmq-server libldap2-dev plpython-9.4
echo "Copying celery scripts"
sudo cp django-mantis/quickstart_files/celery/celeryd_config /etc/default/celeryd
sudo cp django-mantis/quickstart_files/celery/celeryd_initscript /etc/init.d/celeryd
sudo chmod uoa+x /etc/init.d/celeryd
