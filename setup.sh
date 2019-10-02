#!/bin/bash

export DJANGO_SETTINGS_MODULE=rphc_server.settings.development

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

deactivate