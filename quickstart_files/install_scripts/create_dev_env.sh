virtualenv ~/.virtualenvs/mantis_dev
source ~/.virtualenvs/mantis_dev/bin/activate

wget http://xmlsoft.org/sources/libxml2-2.9.1.tar.gz
tar -zxvf libxml2-2.9.1.tar.gz
pip install libxml2-2.9.1/python
rm -r libxml2-2.9.1

git clone https://github/siemens/python-cybox.git
cd python-cybox
git checkout development
pip install -e .
cd ..

git clone https://github/siemens/python-stix.git
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

git clone git@svmdev.cert.siemens.com:django-mantis-dashboard
cd django-mantis-dashboard
git checkout development
pip install -e .
cd ..

git clone git@svmdev.cert.siemens.com:django-mantis-api
cd django-mantis-api
git checkout development
pip install -e .
cd ..

cd django-mantis
pip install -r requirements/testing.txt

echo "Now continue with the quickstart script."

