#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cocuricular.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# K
# Fin practical test

# Settings.py
# 1.	from pathlib import Path
# 2.	import os
# 3.	DEBUG = os.environ.get(‘DJANGO_DEBUG’,’’) != ‘FALSE’
# 4. SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'XXXXXXXXX')

# Create 'Procfile'
# 1. web: gunicorn projectname.wsgi --log-file  -

# terminal 
# 1. pip3 install gunicorn
# 2. pip3 install dj-database-url

# Settings.py
# 1. import dj_database_url
# 2. db_from_env = dj_database_url.config(conn_max_age=500)
# 3. DATABASES['default'].update(db_from_env)

# terminal
# 1. pip3 install psycopg2-binary

# Settings.py
# 1. STATIC_ROOT = BASE_DIR / 'staticfiles'
# 2. STATIC_URL = '/static/'

# terminal
# 1. pip3 install whitenoise

# Settings.py
# 1. MIDDLEWAR = 'whitenoise.middleware.WhiteNoiseMiddleware'

# terminal in the same dir as manage.py
# 1. pip3 freeze > requirements.t
# xt
# Create 'runtime.txt'
# 1. python-3.10.6

# github
# 1. Create repository
# 2. Named it as the projectname

# Right click open Git Bash at your project folder
# 1. git init
# 2. git add .
# 3. git commit -m "first commit"
# 4. git remote add origin https
# 5. git push -u origin master

# pythonanywhere
# 1. On dashboard, click Bash in new console
# 2. git clone https://github.com/USERNAME/REPOSITORY.git
# 3. mkvirtualenv --python=/usr/bin/python3.10 kpmbsite-virtualenv
# 4. pip3 install django
# 5. ls and cd until you see manage.py

# pythonanywhere
# 1. add new web app
# 2. import os
# 3. import sys
# 2. configure path macam raziq ajar path = '/home/Iskndxr/xxxxx'
# 3. os.environ['DJANGO_SETTINGS_MODULE'] = 'projectname.settings'

# Git Bash
# 1. pip install -r requirements.txt
# 2. python manage.py createsuperuser
# 3. python manage.py makemigrations
# 4. python manage.py migrate

# webtab
# 1. set source code 
# Reload web

# Go to settings.py in pythonanywhere
# 1. ALLOWED_HOSTS = ['URL']AsyralDRZ
# Mukhrez@21
