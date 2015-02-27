echo "Starting server"
/etc/init.d/postgresql start 
echo "Creating mantis user"
psql --command "CREATE USER mantis WITH PASSWORD 'mantis';"
#psql --command "ALTER USER mantis CREATEDB;"
psql --command "ALTER USER mantis WITH SUPERUSER;"
echo "Create Database"
psql --command "CREATE DATABASE django OWNER mantis ENCODING 'UTF-8';"
echo "Create language"
psql --command "CREATE LANGUAGE plpythonu;" django
echo "Modifying postgres configuration."
echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.1/main/pg_hba.conf


