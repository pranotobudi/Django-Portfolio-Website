from .base import *

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True
ALLOWED_HOST = []

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pranotobudiwebsite',
        'USER': 'pranotobudiwebsite',
        'PASSWORD': 'passwordpranotobudiwebsite',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}