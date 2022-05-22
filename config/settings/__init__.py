"""
Django settings for sele project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

# from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/


ENV = 'staging'

if ENV == 'test':
    from config.settings.testing_env import (
        TENV_GDAL_DATA, TENV_PROJ_LIB, TENV_PATH, TENV_GDAL_LIBRARY_PATH,
        TENV_SECRET_KEY, TENV_DEBUG, TENV_ALLOWED_HOSTS, TENV_DATABASES,
        TENV_STATIC_URL, TENV_SECURE_SSL_REDIRECT, TENV_MAPBOX_TOKEN, 
    )
    os.environ['GDAL_DATA'] = TENV_GDAL_DATA
    os.environ['PROJ_LIB'] = TENV_PROJ_LIB
    os.environ['PATH'] = TENV_PATH
    GDAL_LIBRARY_PATH = TENV_GDAL_LIBRARY_PATH
    SECRET_KEY = TENV_SECRET_KEY
    DEBUG = TENV_DEBUG
    ALLOWED_HOSTS = TENV_ALLOWED_HOSTS
    DATABASES = TENV_DATABASES
    STATIC_URL = TENV_STATIC_URL
    SECURE_SSL_REDIRECT = TENV_SECURE_SSL_REDIRECT
    MAPBOX_TOKEN = TENV_MAPBOX_TOKEN

elif ENV == 'staging':
    from config.settings.testing_env import (
        TENV_SECRET_KEY, TENV_DEBUG, TENV_ALLOWED_HOSTS, TENV_DATABASES,
        TENV_STATIC_URL, TENV_SECURE_SSL_REDIRECT, TENV_MAPBOX_TOKEN, 
    )
    SECRET_KEY = TENV_SECRET_KEY
    DEBUG = TENV_DEBUG
    ALLOWED_HOSTS = TENV_ALLOWED_HOSTS
    DATABASES = TENV_DATABASES
    STATIC_URL = TENV_STATIC_URL
    SECURE_SSL_REDIRECT = TENV_SECURE_SSL_REDIRECT
    MAPBOX_TOKEN = TENV_MAPBOX_TOKEN

elif ENV == 'production':
    from config.settings.env import (
        ENV_GDAL_DATA, ENV_PROJ_LIB, ENV_PATH, ENV_GDAL_LIBRARY_PATH, 
        ENV_SECRET_KEY, ENV_DEBUG, ENV_ALLOWED_HOSTS, ENV_DATABASES, 
        ENV_STATIC_URL, ENV_STATIC_ROOT, ENV_SECURE_SSL_REDIRECT,
        ENV_SECURE_PROXY_SSL_HEADER, ENV_MAPBOX_TOKEN
    )
    os.environ['GDAL_DATA'] = ENV_GDAL_DATA
    os.environ['PROJ_LIB'] = ENV_PROJ_LIB
    os.environ['PATH'] = ENV_PATH
    GDAL_LIBRARY_PATH = ENV_GDAL_LIBRARY_PATH
    SECRET_KEY = ENV_SECRET_KEY
    DEBUG = ENV_DEBUG
    ALLOWED_HOSTS = ENV_ALLOWED_HOSTS
    DATABASES = ENV_DATABASES
    STATIC_URL = ENV_STATIC_URL
    STATIC_ROOT = ENV_STATIC_ROOT
    SECURE_SSL_REDIRECT = ENV_SECURE_SSL_REDIRECT
    SECURE_PROXY_SSL_HEADER = ENV_SECURE_PROXY_SSL_HEADER
    MAPBOX_TOKEN = ENV_MAPBOX_TOKEN

# Application definition

INSTALLED_APPS = [
    'authentication.apps.AuthenticationConfig',
    'chat.apps.ChatConfig',
    'collectivity.apps.CollectivityConfig',
    'information.apps.InformationConfig',
    'proposition.apps.PropositionConfig',
    'vote.apps.VoteConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
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


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "authentication.CustomUser"
