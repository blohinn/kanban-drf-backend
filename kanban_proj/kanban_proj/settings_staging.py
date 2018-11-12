from .settings import *

ALLOWED_HOSTS = [
    '0.0.0.0'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_db',
        'USER': 'db_username',
        'PASSWORD': 'db_password',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}