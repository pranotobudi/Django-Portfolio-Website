from .base import *

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False
ALLOWED_HOST = ['django-micro-facebook-clone.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd12cjbiskmp7sr',
        'USER': 'nrpfrigvkupqhy',
        'PASSWORD': 'bcb5e85dd342127c30c0880e8b6c6184a051a7368a1639ec27e8a1279c762472',
        'HOST': 'ec2-54-83-50-174.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}