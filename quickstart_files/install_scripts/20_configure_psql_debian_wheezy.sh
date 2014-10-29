if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi
echo "Starting server"
/etc/init.d/postgresql start 

echo "Creating database"
su - postgres -c "psql --command \"CREATE USER mantis WITH PASSWORD 'mantis';\""
su - postgres -c "psql --command \"ALTER USER mantis CREATEDB;\""
su - postgres -c "psql --command \"CREATE USER migrator WITH PASSWORD 'migrator';\""
su - postgres -c "psql --command \"ALTER USER migrator WITH SUPERUSER;\""
su - postgres -c "psql --command \"CREATE DATABASE django OWNER mantis ENCODING 'UTF-8';\""
su - postgres -c "psql --command \"CREATE LANGUAGE plpythonu;\" django"

echo "Modifying postgres configuration."
echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.1/main/pg_hba.conf
exit