from .base import *
import os
import environ


environ.Env.read_env()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME'),
        'USER': 'postgres',
        'PASSWORD': os.environ.get('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

DEFAULT_FROM_EMAIL = os.environ.get('EMAIL')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.wp.pl"
EMAIL_HOST_USER = os.environ.get('EMAIL')
EMAIL_HOST_PASSWORD =os.environ.get('PASS_EMAIL')
EMAIL_PORT = 587

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')
