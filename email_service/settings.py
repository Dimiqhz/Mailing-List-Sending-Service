# -*- coding: utf-8 -*-
import os

# Defining the base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Website basic settings
DEFAULT_FROM_EMAIL = 'noreply@test.com'
TIME_ZONE = 'Europe/Moscow' # Specify your Timezone
USE_TZ = True

# Django basic settings
ALLOWED_HOSTS = ['localhost', '127.0.0.1'] # These hosts are used only for testing, not for production
SECRET_KEY = 'your_secret_key'
ROOT_URLCONF = 'email_service.urls'
# Use this for testing (IT DOESN'T SEND A REAL EMAIL).
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your_smtp_server'
EMAIL_PORT = 465
EMAIL_USE_TLS = True # or False
EMAIL_HOST_USER = 'user_email'
EMAIL_HOST_PASSWORD = 'user_password'
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes', 
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mailing',
    'subscribers',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', 
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
DEBUG = True

# Working with static files
STATIC_URL = '/static/'

# Celery settings
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Satabase settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
