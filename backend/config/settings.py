import os
from pathlib import Path

from django.core.management.utils import get_random_secret_key

from environs import Env

BASE_DIR = Path(__file__).resolve().parent.parent


env = Env()
env.read_env()

SECRET_KEY = env.str('SECRET_KEY', get_random_secret_key())

DEBUG = env.bool('DEBUG', True)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', '127.0.0.1,localhost')


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'order.apps.OrderConfig',
    'rest_framework',
]

REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING': False,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': env.str('SQL_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': env.str('POSTGRES_DB', os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': env.str('POSTGRES_USER', 'admin'),
        'PASSWORD': env.str('POSTGRES_PASSWORD', 'password'),
        'HOST': env.str('SQL_HOST', 'localhost'),
        'PORT': 5432,
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation'
        '.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
        '.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
        '.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
        '.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# orders

ORDERS_GOOGLESHEET_ID = env.str(
    'ORDERS_GOOGLESHEET_ID',
    '1AkbjncKtr9_xW3mFcpxX9E1FDoFyn0sAbomPFIUxmDo',
)
ORDERS_GOOGLESHEET_RANGE = 'A:D'
