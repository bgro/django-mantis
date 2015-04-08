cd /home/mantis/ti
virtualenv ~/.virtualenvs/mantis_dev
source ~/.virtualenvs/mantis_dev/bin/activate
your_proxy=YOURPROXY:PORT
wget http://xmlsoft.org/sources/libxml2-2.9.1.tar.gz
tar -zxvf libxml2-2.9.1.tar.gz
cd libxml2-2.9.1/python
(pip install -e . --proxy=$your_proxy 2>&1) | tee -a /home/mantis/ti/install.log
cd ../..
rm -r libxml2-2.9.1

git clone https://github.com/CybOXProject/python-cybox.git
cd python-cybox
git fetch --tags
git checkout v2.1.0.10
(pip install -e . --proxy=$your_proxy 2>&1) | tee -a /home/mantis/ti/install.log
cd ..

git clone https://github.com/STIXProject/python-stix.git
cd python-stix
git fetch --tags
git checkout v1.1.1.4
(pip install -e . --proxy=$your_proxy 2>&1) | tee -a /home/mantis/ti/install.log
cd ..

git clone https://github.com/siemens/django-dingos.git
cd django-dingos
git checkout development
(pip install -e . --proxy=$your_proxy 2>&1) | tee -a /home/mantis/ti/install.log
cd ..

git clone https://github.com/siemens/django-mantis-core.git
cd django-mantis-core
git checkout development
(pip install -e . --proxy=$your_proxy 2>&1) | tee -a /home/mantis/ti/install.log
cd ..

git clone https://github.com/siemens/django-mantis-openioc-importer.git
cd django-mantis-openioc-importer
git checkout development
(pip install -e . --proxy=$your_proxy 2>&1) | tee -a /home/mantis/ti/install.log
cd ..

git clone https://github.com/siemens/django-mantis-stix-importer.git
cd django-mantis-stix-importer
git checkout development
(pip install -e . --proxy=$your_proxy 2>&1) | tee -a /home/mantis/ti/install.log
cd ..


git clone https://github.com/siemens/django-mantis-iodef-importer.git
cd django-mantis-iodef-importer
git checkout development
(pip install -e . --proxy=$your_proxy 2>&1) | tee -a /home/mantis/ti/install.log
cd ..

git clone https://github.com/siemens/django-dingos-authoring.git
cd django-dingos-authoring
git checkout development
(pip install -e . --proxy=$your_proxy 2>&1) | tee -a /home/mantis/ti/install.log
cd ..

git clone https://github.com/siemens/django-mantis-authoring.git
cd django-mantis-authoring
git checkout development
(pip install -e . --proxy=$your_proxy 2>&1) | tee -a /home/mantis/ti/install.log
cd ..

#git clone https://github.com/siemens/django-mantis-api.git
#cd django-mantis-api
#git checkout development
#(pip install -e . --proxy=$your_proxy 2>&1) | tee -a /home/mantis/ti/install.log
#cd ..

#git clone https://github.com/siemens/django-mantis-api-siemens.git
#cd django-mantis-api-siemens
#git checkout development
#(pip install -e . --proxy=$your_proxy 2>&1) | tee -a /home/mantis/ti/install.log
#cd ..

git clone https://github.com/siemens/django-mantis-actionables.git
cd django-mantis-actionables
git checkout development
(pip install -e . --proxy=$your_proxy 2>&1) | tee -a /home/mantis/ti/install.log
cd ..

git clone https://github.com/siemens/django-mantis-malte.git
cd django-mantis-malte
git checkout development
(pip install -e . --proxy=$your_proxy 2>&1) | tee -a /home/mantis/ti/install.log
cd ..

cd django-mantis
(pip install -r requirements/testing.txt 2>&1) | tee -a /home/mantis/ti/install.log

(python manage.py migrate --noinput --traceback --settings=mantis.settings.local_psql 2>&1) | tee -a /home/mantis/ti/install.log
(python manage.py collectstatic --noinput --settings=mantis.settings.local_psql  --trace 2>&1) | tee -a /home/mantis/ti/install.log
(python manage.py mantis_openioc_set_naming --settings=mantis.settings.local_psql  --trace 2>&1) | tee -a /home/mantis/ti/install.log
(python manage.py mantis_stix_set_naming --settings=mantis.settings.local_psql  --trace 2>&1) | tee -a /home/mantis/ti/install.log
(python -c "\
import os;\
os.environ['DJANGO_SETTINGS_MODULE'] = 'mantis.settings.local_psql';\
from django.conf import settings;\
from django.contrib.auth.models import User;\
u = User(username='admin');\
u.set_password('admin');\
u.is_superuser = True;\
u.is_staff = True ;\
u.save()" 2>&1) | tee -a /home/mantis/ti/install.log
