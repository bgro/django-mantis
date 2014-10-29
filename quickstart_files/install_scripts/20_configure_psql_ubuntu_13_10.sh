echo "Starting server"
/etc/init.d/postgresql start 
echo "Creating database"
psql --command "CREATE USER mantis WITH PASSWORD 'mantis';"
psql --command "ALTER USER mantis CREATEDB;"
psql --command "CREATE USER migrator WITH PASSWORD 'migrator';"
psql --command "ALTER USER migrator WITH SUPERUSER;"
psql --command "CREATE DATABASE django OWNER mantis ENCODING 'UTF-8';"
psql --command "CREATE LANGUAGE plpythonu;" django
echo "Modifying postgres configuration."
echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.1/main/pg_hba.conf


