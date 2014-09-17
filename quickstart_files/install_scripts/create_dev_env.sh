virtualenv ~/.virtualenvs/mantis_dev2
source ~/.virtualenvs/mantis_dev/bin/activate

wget http://xmlsoft.org/sources/libxml2-2.9.1.tar.gz
tar -zxvf libxml2-2.9.1.tar.gz
pip install libxml2-2.9.1/python
rm -r libxml2-2.9.1

mkdir ti
cd ti

git clone git@svmdev.cert.siemens.com:python-cybox.git
cd python-cybox
git checkout development
pip install -e .
cd ..

git clone git@svmdev.cert.siemens.com:python-stix.git
cd python-stix
git checkout development
pip install -e .
cd ..

git clone git@svmdev.cert.siemens.com:django-dingos.git
cd django-dingos
git checkout development
pip install -e .
cd ..

git clone git@svmdev.cert.siemens.com:django-mantis-core.git
cd django-mantis-core
git checkout development
pip install -e .
cd ..

git clone git@svmdev.cert.siemens.com:django-mantis-openioc-importer.git
cd django-mantis-openioc-importer
git checkout development
pip install -e .
cd ..

git clone git@svmdev.cert.siemens.com:django-mantis-stix-importer.git
cd django-mantis-stix-importer
git checkout development
pip install -e .
cd ..


git clone git@svmdev.cert.siemens.com:django-mantis-iodef-importer.git
cd django-mantis-iodef-importer
git checkout development
pip install -e .
cd ..

git clone git@svmdev.cert.siemens.com:django-dingos-authoring.git
cd django-dingos-authoring
git checkout development
pip install -e .
cd ..

git clone git@svmdev.cert.siemens.com:django-mantis-authoring.git
cd django-mantis-authoring
git checkout development
pip install -e .
cd ..

git clone git@svmdev.cert.siemens.com:django-mantis-dashboard.git
cd django-mantis-dashboard
git checkout development
pip install -e .
cd ..

git clone git@svmdev.cert.siemens.com:django-mantis-api.git
cd django-mantis-api
git checkout development
pip install -e .
cd ..

git clone git@svmdev.cert.siemens.com:django-mantis.git
cd django-mantis
git checkout development
pip install -r requirements/testing.txt

echo "Now continue with the quickstart script."

