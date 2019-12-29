from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['elsope.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd3658hoffoq09b',
        'USER': 'awadvyvvtwtpdm',
        'PASSWORD': 'a11c28c8c2256bd5880edb9a41c9dfb069b9aeae8a5864454d1f7cd096d9c7ac',
        'HOST': 'ec2-174-129-22-22.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

