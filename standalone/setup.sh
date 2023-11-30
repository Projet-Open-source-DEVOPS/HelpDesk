#!/bin/sh

# if docker.env does not exist create it from the template
if [ ! -f docker.env ]; then
    cp docker.env.template docker.env
fi

    echo "DJANGO_HELPDESK_SECRET_KEY=$(openssl rand -hex 32)" > docker.env
    echo "POSTGRES_PASSWORD=$(openssl rand -hex 32)" >> docker.env
