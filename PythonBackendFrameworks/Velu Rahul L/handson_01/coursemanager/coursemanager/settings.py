"""
=========================================================
File : settings.py

Purpose:
This file contains the global configuration for the
Course Management Django project.

It is responsible for:
1. Database configuration
2. Installed applications
3. Middleware configuration
4. Template settings
5. Static file configuration
6. Security and project-level settings
=========================================================
"""

from pathlib import Path

# Base directory of the Django project
BASE_DIR = Path(__file__).resolve().parent.parent


# Security Configuration

SECRET_KEY = "django-insecure-jlio-hzoa%6exthtu!+j-jaxgk!)-wp1eg&#4s-jflk#aen($v"

DEBUG = True

ALLOWED_HOSTS = []


# Installed Applications
INSTALLED_APPS = [

    # Django Default Apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Local Application
    "courses",

]


# Middleware Configuration
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# Root URL Configuration
ROOT_URLCONF = "coursemanager.urls"


# Template Configuration

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# WSGI Application
WSGI_APPLICATION = "coursemanager.wsgi.application"


# Database Configuration for the handson
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password Validators
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
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True



# Static Files
STATIC_URL = "static/"


# Default Primary Key
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
