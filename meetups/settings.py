"""
Django settings for meetups project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os

from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# Common information
SITE_NAME = "Meetups"
SITE_DOMAIN = 'meetups.quickmediasolutions.com'


#################
# Core settings #
#################

DEBUG = 'DEBUG' in os.environ
SECRET_KEY = os.environ.get('SECRET_KEY', 'DEBUG' if DEBUG else '')

ALLOWED_HOSTS = [] if DEBUG else [SITE_DOMAIN]
USE_X_FORWARDED_HOST = True

ROOT_URLCONF = 'meetups.urls'
WSGI_APPLICATION = 'meetups.wsgi.application'

USE_TZ = True
TIME_ZONE = 'UTC'


##################
# Applications #
##################

INSTALLED_APPS = [

    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party apps
    'rest_framework',

    # Project apps
    'ui',
]


############
# Database #
############

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        },
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('DB_NAME', 'postgres'),
            'USER': os.environ.get('DB_USER', 'postgres'),
            'PASSWORD': os.environ.get('DB_PASSWORD', ''),
            'HOST': os.environ.get('DB_HOST', 'postgres'),
        },
    }


#########
# Email #
#########

ADMINS = [
    ("Nathan Osman", "nathan.osman@gmail.com"),
]

DEFAULT_FROM_EMAIL = SERVER_EMAIL = "{} <donotreply@{}>".format(
    SITE_NAME,
    SITE_DOMAIN,
)

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'pyhectane.django.HectaneBackend'
    HECTANE_HOST = 'hectane'


###############
# Media files #
###############

if DEBUG:
    MEDIA_ROOT = BASE_DIR / 'media'
else:
    MEDIA_ROOT = '/srv/media/'

MEDIA_URL = '/media/'


################
# Static files #
################

STATIC_ROOT = '/srv/static/'
STATIC_URL = '/static/'

if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static',
    ]


#############
# Templates #
#############

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


########
# Misc #
########

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
