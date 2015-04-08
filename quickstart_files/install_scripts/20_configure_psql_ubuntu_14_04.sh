echo "Starting server"
sudo /etc/init.d/postgresql start 
echo "Creating mantis user"
sudo -u postgres psql --command "CREATE USER mantis WITH PASSWORD 'mantis';"
#sudo -u postgres psql --command "ALTER USER mantis CREATEDB;"
sudo -u postgres psql --command "ALTER USER mantis WITH SUPERUSER;"
echo "Create Database"
sudo -u postgres psql --command "CREATE DATABASE django OWNER mantis ENCODING 'UTF-8';"
echo "Create language"
sudo -u postgres psql --command "CREATE LANGUAGE plpythonu;" django
echo "Modifying postgres configuration."
echo "host all  all    0.0.0.0/0  md5" | sudo tee -a /etc/postgresql/9.4/main/pg_hba.conf


