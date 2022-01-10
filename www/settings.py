"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from distutils.util import strtobool
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', "n3r4zq2uum(ouciq8od=$q1!$zxl_&z#fa*el(r!kp+wnus^=c")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(strtobool(os.getenv('DEBUG', False)))

if DEBUG:
    ALLOWED_HOSTS = [
        'teambuilding.tasting.local']
else:
    ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.forms',
    'django_extensions',
    'debug_toolbar',
    'icalendar',
    'phonenumber_field',
    'lib.postaladdress',
    'teambuilding.site',
    'teambuilding.accounts',
    'teambuilding.users',
    'teambuilding.events',
    'teambuilding.products',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'www.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates', ],
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

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

WSGI_APPLICATION = 'www.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'it-IT'

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True

DATETIME_INPUT_FORMATS = [
    '%Y-%d-%m %H:%M:%S',     # '2006-10-25 14:30:59'
    '%Y-%d-%m %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
    '%Y-%d-%m %H:%M',        # '2006-10-25 14:30'
    '%d/%m/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
    '%d/%m/%Y %H:%M:%S.%f',  # '10/25/2006 14:30:59.000200'
    '%d/%m/%Y %H:%M',        # '10/25/2006 14:30'
    '%d/%m/%y %H:%M:%S',     # '10/25/06 14:30:59'
    '%d/%m/%y %H:%M:%S.%f',  # '10/25/06 14:30:59.000200'
    '%d/%m/%y %H:%M',        # '10/25/06 14:30'
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#

AUTH_USER_MODEL = 'accounts.UserAccount'

LOGIN_URL = 'login'

LOGIN_REDIRECT_URL = 'home'


# Debug toolbar

def show_toolbar(request):
    return DEBUG


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}

# Mail configuration

EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
MAILER_EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.netbuilder.local')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', '1025'))
EMAIL_USE_TLS = bool(strtobool(os.getenv('EMAIL_USE_TLS', 'False')))
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'server@smtp.netbuilder.local')
