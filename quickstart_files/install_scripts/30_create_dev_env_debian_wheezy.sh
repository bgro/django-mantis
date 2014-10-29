virtualenv ~/.virtualenvs/mantis_dev
source ~/.virtualenvs/mantis_dev/bin/activate

wget http://xmlsoft.org/sources/libxml2-2.8.0.tar.gz
tar -zxvf libxml2-2.8.0.tar.gz
pip install -e libxml2-2.8.0/python
rm -r libxml2-2.8.0.tar.gz

git clone https://github.com/siemens/python-cybox.git
cd python-cybox
git checkout development
pip install -e .
cd ..

git clone https://github.com/siemens/python-stix.git
cd python-stix
git checkout development
pip install -e .
cd ..

git clone git@svmdev.cert.siemens.com:django-dingos
cd django-dingos
git checkout development
pip install -e .
cd ..

git clone git@svmdev.cert.siemens.com:django-mantis-core
cd django-mantis-core
git checkout development
pip install -e .
cd ..

git clone git@svmdev.cert.siemens.com:django-mantis-openioc-importer
cd django-mantis-openioc-importer
git checkout development
pip install -e .
cd ..

git clone git@svmdev.cert.siemens.com:django-mantis-stix-importer
cd django-mantis-stix-importer
git checkout development
pip install -e .
cd ..


git clone git@svmdev.cert.siemens.com:django-mantis-iodef-importer
cd django-mantis-iodef-importer
git checkout development
pip install -e .
cd ..

git clone git@svmdev.cert.siemens.com:django-dingos-authoring
cd django-dingos-authoring
git checkout development
pip install -e .
cd ..

git clone git@svmdev.cert.siemens.com:django-mantis-authoring
cd django-mantis-authoring
git checkout development
pip install -e .
cd ..

# Siemens specific

#### FAIL ldap
git clone git@svmdev.cert.siemens.com:django-mantis-api
cd django-mantis-api
git checkout development
pip install -e .
cd ..


git clone git@svmdev.cert.siemens.com:django-mantis-api-siemens
cd django-mantis-api-siemens
git checkout development
pip install -e .
cd ..


git clone git@svmdev.cert.siemens.com:django-mantis-dashboard
cd django-mantis-dashboard
git checkout development
pip install -e .
cd ..


git clone git@svmdev.cert.siemens.com:django-mantis-dataimport-siemens
cd django-mantis-dataimport-siemens
git checkout development
pip install -e .
cd ..



cd django-mantis
pip install -r requirements/testing.txt

python manage.py migrate --noinput --traceback --settings=mantis.settings.local_psql
#works if ``south`` is disabled
python manage.py collectstatic --noinput --settings=mantis.settings.local_psql  --trace
python manage.py mantis_openioc_set_naming --settings=mantis.settings.local_psql  --trace 
python manage.py mantis_stix_set_naming --settings=mantis.settings.local_psql  --trace
python -c "\
import os;\
os.environ['DJANGO_SETTINGS_MODULE'] = 'mantis.settings.local_psql';\
from django.conf import settings;\
from django.contrib.auth.models import User;\
u = User(username='admin');\
u.set_password('admin');\
u.is_superuser = True;\
u.is_staff = True ;\
u.save()"

