from pathlib import Path
import os
import sys
import dj_database_url

if os.path.isfile('env.py'):
    import env

DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'
LOGIN_REDIRECT_URL = 'books'
ROOT_URLCONF = 'library.urls'
WSGI_APPLICATION = 'library.wsgi.application'
SITE_ID = 1
USE_TZ = True
USE_I18N = True
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
STATIC_URL = 'static/'
ACCOUNT_EMAIL_VERIFICATION = 'none'
SECRET_KEY = os.environ.get('SECRET_KEY')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
STATICFILES_DIRS = [os.path.join(BASE_DIR, STATIC_URL), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
CSRF_TRUSTED_ORIGINS = ["https://*.codeanyapp.com", "https://*.herokuapp.com"]
ALLOWED_HOSTS = [".herokuapp.com", "127.0.0.1", "localhost"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'cloudinary',
    'book.apps.BookConfig',
    'author.apps.AuthorConfig',
    'reader.apps.ReaderConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

if 'test' in sys.argv:
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'

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
