cd /home/mantis/ti
mkdir sample_data
cd sample_data
mkdir first2014
cd first2014
wget http://jvnrss.ise.chuo-u.ac.jp/~masato/F2014/F2014.xml
cd ..
mkdir apt1
cd apt1
wget  http://stix.mitre.org/downloads/APT1-STIX.zip
unzip APT1-STIX.zip
cd ..
mkdir mitre
cd mitre
wget https://raw.github.com/STIXProject/schemas/version_1.1.1/samples/STIX_Domain_Watchlist.xml
wget https://raw.github.com/STIXProject/schemas/version_1.1.1/samples/STIX_Email_wAttachment.xml
wget https://raw.github.com/STIXProject/schemas/version_1.1.1/samples/STIX_Email_wFullAttachment.xml
wget https://raw.github.com/STIXProject/schemas/version_1.1.1/samples/STIX_Email_wLink.xml
wget https://raw.github.com/STIXProject/schemas/version_1.1.1/samples/STIX_FileHash_Watchlist.xml
wget https://raw.github.com/STIXProject/schemas/version_1.1.1/samples/STIX_Indicator_Snort.xml
wget https://raw.github.com/STIXProject/schemas/version_1.1.1/samples/STIX_IP_Watchlist.xml
wget https://raw.github.com/STIXProject/schemas/version_1.1.1/samples/STIX_Malware_Sample.xml
wget https://raw.github.com/STIXProject/schemas/version_1.1.1/samples/STIX_URL_Watchlist.xml
cd ..

cd /home/mantis/ti/django-mantis

source /home/mantis/.virtualenvs/mantis_dev/bin/activate

python manage.py mantis_stix_import /home/ti/sample_data/first2014/F2014.xml --settings=mantis.settings.local_psql
python manage.py mantis_stix_import /home/ti/sample_data/apt1/Mandiant_APT1_Report.xml --settings=mantis.settings.local_psql
python manage.py mantis_stix_import /home/ti/sample_data/mitre/*.xml --settings=mantis.settings.local_psql

