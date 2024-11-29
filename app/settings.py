from os import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# Security settings
SECRET_KEY = environ.get("SECRET_KEY", "secret")
DEBUG = environ.get("DEBUG", "false").lower() == "true"

ALLOWED_HOSTS = []
ALLOWED_HOSTS += environ.get("ALLOWED_HOSTS", "").split(",")

CSRF_TRUSTED_ORIGINS = []
CSRF_TRUSTED_ORIGINS += environ.get("CSRF_TRUSTED_ORIGINS", "").split(",")


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "cms",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "app.wsgi.application"


# Database

RDS_ADMIN_SEARCH_PATH = environ.get("RDS_ADMIN_SEARCH_PATH", "admin,public")
RDS_CMS_SEARCH_PATH = environ.get("RDS_CMS_SEARCH_PATH", "public")
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "OPTIONS": {"options": "-c search_path=" + RDS_ADMIN_SEARCH_PATH},
        "HOST": environ.get("RDS_HOSTNAME"),
        "PORT": environ.get("RDS_PORT"),
        "NAME": environ.get("RDS_DB_NAME"),
        "USER": environ.get("RDS_USERNAME"),
        "PASSWORD": environ.get("RDS_PASSWORD"),
    },
    "cms": {
        "ENGINE": "django.db.backends.postgresql",
        "OPTIONS": {"options": "-c search_path=" + RDS_CMS_SEARCH_PATH},
        "HOST": environ.get("RDS_HOSTNAME"),
        "PORT": environ.get("RDS_PORT"),
        "NAME": environ.get("RDS_DB_NAME"),
        "USER": environ.get("RDS_USERNAME"),
        "PASSWORD": environ.get("RDS_PASSWORD"),
    },
}
DATABASE_ROUTERS = ["app.router.Router"]
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Internationalization

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = "/static/"
STATIC_ROOT = "/root/.collected_static"