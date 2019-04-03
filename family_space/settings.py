"""
Django settings for family_space project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+4##tnsmrsvxy(aehvwz0pdmu%o*g^k_=iq76-(i&h3jhswedr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_swagger',
    'api.apiauthapp',
    'api.apiuserapp',
    'api.core',
    'groupapp',
    'shoppingapp',
    'chatapp',
    'eventapp',
    'userapp',
    'taskapp',
    'authapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'family_space.urls'

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

WSGI_APPLICATION = 'family_space.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGES = [
    ('en', _('English')),
    ('ru', _('Русский')),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'api.core.handlers.core_exception_handler',
    'NON_FIELD_ERRORS_KEY': 'error',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'api.apiauthapp.backends.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
}

# Время жизни токена в днях
EXP_TOKEN = 365

SWAGGER_SETTINGS = {
    'APIS_SORTER': 'alpha',
    'api_version': '0.1',
    'enabled_methods': [
        'get',
        'post',
        'put',
        'delete',
    ],
    'SECURITY_DEFINITIONS': {
        "api_key": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT authorization"
        },
    },
    'USE_SESSION_AUTH': False,
    'SHOW_REQUEST_HEADERS': True,
    'JSON_EDITOR': True
}

AUTH_USER_MODEL = 'authapp.User'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'authapp:signin'

DOMAIN_NAME = 'http://localhost:8000'
EMAIL_HOST = 'localhost'
EMAIL_PORT = '25'
EMAIL_HOST_USER = 'django@geekshop.local'
EMAIL_HOST_PASSWORD = 'geekshop'
EMAIL_USE_SSL = False
EMAIL_VERIFY_VIEW = 'authapp:verify'

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'tmp/email-messages/')

try:
    from local_settings import *
except ImportError:
    pass

STATIC_ROOT = os.path.join(BASE_DIR, 'authapp/static/')
