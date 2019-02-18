from .base import *

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False
ALLOWED_HOST = ['pranotobudi-website.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbltu8bfhoh35v',
        'USER': 'iijrpjzngvwxra',
        'PASSWORD': 'e89d41465947093ddf6dfddb2010389997e01d87851780e17bd5e4e12ec5779b',
        'HOST': 'ec2-174-129-224-157.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}