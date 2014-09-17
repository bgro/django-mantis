sudo apt-get install libxml2 libxml2-dev python-dev libxslt1-dev python-virtualenv python-pip postgresql postgresql-server-dev-9.1 psycopg2 rabbitmq-server
sudo cp ../celery/celeryd_config /etc/default/celeryd
sudo cp ../celery/celeryd_initscript /etc/init.d/celeryd
sudo chmod uoa+x /etc/init.d/celeryd
