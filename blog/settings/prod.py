from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_comision6',
        'USER':'rodridg91',
        'PASSWORD':'rootroot',
        'HOST': 'rodridg91.mysql.pythonanywhere-services.com',
        'PORT':''
    }
}