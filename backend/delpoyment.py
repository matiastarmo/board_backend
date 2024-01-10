import os
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = ['*']
CORS_ALLOWED_ORIGINS = ['*']
SECRET_KEY = os.environ.get('SECRET_KEY')


DEBUG = False
