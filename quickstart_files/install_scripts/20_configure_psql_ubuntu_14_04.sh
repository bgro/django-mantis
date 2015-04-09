#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi
echo "Starting server"
/etc/init.d/postgresql start 
echo "Initialize database."
su postgres -c "psql -f init_postgres.sql"
echo "Modifying postgres configuration."
echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.4/main/pg_hba.conf


