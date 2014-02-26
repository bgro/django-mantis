echo "Upgrading from v0.1.0 to v0.2.0"
echo "==============================="
echo ""
echo "Adding tables for models that have been introduced in v0.2.0"
echo "------------------------------------------------------------"
python manage.py migrate dingos --traceback --settings=mantis.settings.local
echo ""
echo "Adding static files that have been introduced in v0.2.0"
echo "------------------------------------------------------------"
python manage.py collectstatic --settings=mantis.settings.local  --trace

