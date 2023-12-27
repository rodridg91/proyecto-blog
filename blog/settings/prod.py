from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['rodridg91.pythonanywhere.com']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rodridg91$default',
        'USER':'rodridg91',
        'PASSWORD':'info2023',
        'HOST': 'rodridg91.mysql.pythonanywhere-services.com',
        'PORT':''
    }
}