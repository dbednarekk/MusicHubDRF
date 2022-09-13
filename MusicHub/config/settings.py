"""
Django settings for MusicHub project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from os.path import join
from distutils.util import strtobool
from configurations import Configuration

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Common(Configuration):
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!

    # SECURITY WARNING: don't run with debug turned on in production!
    # Set DEBUG to False as a default for safety
    # https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = False
    SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

    ALLOWED_HOSTS = ["*"]

    # Email
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

    # Application definition
    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        # Third party apps
        "rest_framework",
        "django_filters",
        "drf_yasg",
        "oauth2_provider",
        "social_django",
        "drf_social_oauth2",
        # apps
        "MusicHub.users",
        "MusicHub.main",
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ROOT_URLCONF = "MusicHub.urls"

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.1/howto/static-files/
    STATIC_ROOT = os.path.normpath(join(os.path.dirname(BASE_DIR), "static"))
    STATICFILES_DIRS = []
    STATIC_URL = "/static/"
    STATICFILES_FINDERS = (
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    )
    # Media files
    MEDIA_ROOT = join(os.path.dirname(BASE_DIR), "media")
    MEDIA_URL = "/media/"

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": STATICFILES_DIRS,
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                    "social_django.context_processors.backends",
                    "social_django.context_processors.login_redirect",
                ]
            },
        }
    ]

    WSGI_APPLICATION = "MusicHub.wsgi.application"

    # Database
    # https://docs.djangoproject.com/en/4.1/ref/settings/#databases

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "postgres",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "localhost",
            "PORT": "5432",
        }
    }

    # Custom user app
    AUTH_USER_MODEL = "users.User"

    # Password validation
    # https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/4.1/topics/i18n/

    LANGUAGE_CODE = "en-us"

    TIME_ZONE = "UTC"
    USE_I18N = False
    USE_L10N = True
    USE_TZ = True
    LOGIN_REDIRECT_URL = "/"

    # Default primary key field type
    # https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

    # Django Rest Framework
    REST_FRAMEWORK = {
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
        "PAGE_SIZE": int(os.getenv("DJANGO_PAGINATION_LIMIT", 10)),
        "DATETIME_FORMAT": "%Y-%m-%dT%H:%M:%S%z",
        "DEFAULT_RENDERER_CLASSES": (
            "rest_framework.renderers.JSONRenderer",
            "rest_framework.renderers.BrowsableAPIRenderer",
        ),
        "DEFAULT_PERMISSION_CLASSES": [
            "rest_framework.permissions.AllowAny",
        ],
        "DEFAULT_AUTHENTICATION_CLASSES": (
            "oauth2_provider.contrib.rest_framework.OAuth2Authentication",  # django-oauth-toolkit >= 1.0.0
            "drf_social_oauth2.authentication.SocialAuthentication",
        ),
        "EXCEPTION_HANDLER": "MusicHub.main.exception_handler.custom_exception_handler",
    }
    AUTHENTICATION_BACKENDS = (
        # Google OAuth2
        "social_core.backends.google.GoogleOAuth2",
        "drf_social_oauth2.backends.DjangoOAuth2",
        "django.contrib.auth.backends.ModelBackend",
    )
    SOCIAL_AUTH_PIPELINE = (
        "social_core.pipeline.social_auth.social_details",
        "social_core.pipeline.social_auth.social_uid",
        "social_core.pipeline.social_auth.auth_allowed",
        "social_core.pipeline.social_auth.social_user",
        "social_core.pipeline.user.get_username",
        "social_core.pipeline.social_auth.associate_by_email",
        "social_core.pipeline.user.create_user",
        "social_core.pipeline.social_auth.associate_user",
        "social_core.pipeline.social_auth.load_extra_data",
        "social_core.pipeline.user.user_details",
    )
    # Google configuration
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = (
        "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"
    )
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "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"

    # Define SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE to get extra permissions from Google.
    SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile",
    ]

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "django.server": {
                "()": "django.utils.log.ServerFormatter",
                "format": "[%(asctime)s] %(message)s",
            },
            "verbose": {
                "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
            },
            "simple": {"format": "%(levelname)s %(message)s"},
        },
        # "filters": {
        #     "require_debug_true": {
        #         "()": "django.utils.log.RequireDebugTrue",
        #     },
        # },
        "handlers": {
            "django.server": {
                "level": "INFO",
                "class": "logging.StreamHandler",
                "formatter": "django.server",
            },
            "file": {
                "level": "INFO",
                "class": "logging.FileHandler",
                "filename": "general.log",
                "formatter": "simple",
            },
            "file_error": {
                "level": "ERROR",
                "class": "logging.FileHandler",
                "filename": "error.log",
                "formatter": "verbose",
            },
        },
        "loggers": {
            "django": {
                "handlers": ["django.server", "file", "file_error"],
                "propagate": True,
            },
            "django.server": {
                "handlers": ["django.server", "file", "file_error"],
                "level": "INFO",
                "propagate": False,
            },
            "django.request": {
                "handlers": ["django.server", "file", "file_error"],
                "level": "INFO",
                "propagate": False,
            },
            "django.db.backends": {
                "handlers": ["django.server", "file", "file_error"],
                "level": "INFO",
            },
        },
    }
    EMAIL_HOST = "smtp.sendgrid.net"
    EMAIL_PORT = "587"
    EMAIL_HOST_USER = "apikey"
    EMAIL_HOST_PASSWORD = os.getenv("DJANGO_EMAIL_KEY")
