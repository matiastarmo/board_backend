import os
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = ['*']
CORS_ALLOWED_ORIGINS = ['*']
CSRF_TRUSTED_ORIGINS = ['*']
SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME'), 
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'), 
        'PORT': os.environ.get('DB_PORT'),
    }
}



