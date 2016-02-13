# -*- coding: utf-8 -*-
from os.path import join, abspath, dirname
from django.utils.translation import ugettext_lazy as _
from configurations import Configuration, values


class Common(Configuration):
    """
    Basic configuration
    """

    BASE_DIR = dirname(dirname(dirname(abspath(__file__))))

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Third party apps
        'rest_framework',            # utilities for rest apis
        'rest_framework.authtoken',  # token authentication

        # Custom apps
        'api',
    )

    # https://docs.djangoproject.com/en/1.8/topics/http/middleware/
    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.security.SecurityMiddleware'
    )

    ROOT_URLCONF = 'base.urls'

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

    SECRET_KEY = values.SecretValue()
    WSGI_APPLICATION = 'base.wsgi.application'

    # Migrations
    MIGRATION_MODULES = {
        'sites': 'contrib.sites.migrations'
    }

    # Set DEBUG to False as a default for safety
    # https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = values.BooleanValue(default=False)

    MANAGERS = (
        ("Author", 'sebastian.manger@cde.unibe.ch'),
    )

    # Postgres
    DATABASES = values.DatabaseURLValue()

    # Time and i18n settings
    TIME_ZONE = 'Europe/Zurich'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    SITE_ID = 1
    LOGIN_REDIRECT_URL = '/'

    # English only
    LANGUAGES = (
        ('en', _('English')),
    )

    # Static Files
    STATIC_ROOT = join(dirname(BASE_DIR), 'staticfiles')
    STATIC_URL = '/static/'
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    # Media files
    MEDIA_ROOT = join(dirname(BASE_DIR), 'media')
    MEDIA_URL = '/media/'

    # Logging
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True
            },
        }
    }

    # Django Rest Framework
    REST_FRAMEWORK = {
        'DATETIME_FORMAT': '%Y-%m-%dT%H:%M:%S%z',
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ),
    }

    MYSWISSALPS_API_URL = values.Value(
        environ_prefix='',
        default='http://www.myswissalps.ch'
    )
    API_CALL_RETRIES = values.IntegerValue(
        environ_prefix='',
        default=5
    )

