from django.utils.translation import ugettext_lazy as _
from mozillaz.base import INSTALLED_APPS, MIDDLEWARE  # NOQA
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Not@So#Secret'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
DEBUG_TOOLBAR = False

ALLOWED_HOSTS = ['www.mozillaz.org']


# Application definition
ROOT_URLCONF = 'mozillaz.urls'
APPEND_SLASH = True
# User settings
AUTH_USER_MODEL = 'user.User'

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

WSGI_APPLICATION = 'mozillaz.wsgi.application'
PAGINATION_LIMIT = 25
LOGIN_URL = "/login/"
LOGOUT_REDIRECT_URL = "/"
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o755
FILE_UPLOAD_PERMISSIONS = 0o644

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
LANGUAGES = (
    ('az', _("Azerbaijani")),
    ('en', _('English')),
)
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
LANGUAGE_CODE = 'az'

TIME_ZONE = 'Asia/Baku'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, STATIC_URL.strip("/"))

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_URL.strip("/"))

try:
    from local_settings import *  # NOQA
except ImportError as e:
    if "local_settings" not in str(e):
        raise e
