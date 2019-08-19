#!/bin/bash

export DJANGO_SETTINGS_MODULE=rphc_server.settings.development

# Python Virtual Environment
python3.7 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py create_test_data

deactivate
