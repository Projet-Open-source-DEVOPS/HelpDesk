#!/bin/bash
# Install extra deps from /opt/extra-deps.txt if it exists
if [ -f /opt/extra-dependencies.txt ]; then
    pip install -r /opt/extra-dependencies.txt
fi

cd /opt/django-helpdesk/standalone/
if python manage.py showmigrations | grep '\[ \]\|^[a-z]' | grep '[  ]' -B 1; then
    python manage.py migrate --noinput                # Apply database migrations
fi

#Apply some datas for exemple
python3 /opt/django-helpdesk/standalone/manage.py loaddata /opt/django-helpdesk/demo/demodesk/fixtures/demo.json
DJANGO_SUPERUSER_PASSWORD=Test1234 python3 /opt/django-helpdesk/standalone/manage.py createsuperuser --username admin --email helpdesk@example.com --noinput

#Apply group and permissions
python3 /opt/django-helpdesk/standalone/manage.py create_permissions_group
echo Creating the group permissions Client and Provider success.

#Create a client and a provider for test
python3 /opt/django-helpdesk/standalone/manage.py create_client_and_provider

echo Creating 2 user : One with Provider group permissions and other with the Client group permissions
# Starting cron to check emails
printenv > /etc/env
env | awk -F= '{printf "export %s=\"%s\"\n", $1, $2}' > /etc/env
cron &&
# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn standalone.config.wsgi:application \
	--name django-helpdesk \
	--bind 0.0.0.0:${GUNICORN_PORT:-"8000"} \
	--workers ${GUNICORN_NUM_WORKERS:-"6"} \
	--timeout ${GUNICORN_TIMEOUT:-"60"} \
	--preload \
	--reload \
	--log-level=debug \
	--log-file=/opt/django-helpdesk/gunicorn-log.log \
	--access-logfile=/opt/django-helpdesk/gunicorn-log-access.log \
	"$@"