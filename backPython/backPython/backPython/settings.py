"""
Django settings for backPython project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from settings_json import get_setting
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_setting('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_setting('debug')  #True
CORS_ALLOW_ALL_ORIGINS=get_setting('CORS_ALLOW_ALL_ORIGINS')
ALLOWED_HOSTS = get_setting('hosts')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'department',
    'employee',
    'rest_framework',
    'djoser',
    'rest_framework.authtoken',
    'corsheaders' ,
    'bcrypt',
]



PASSWORD_HASHED = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHaser',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]

LOGGING = {
    'version' : 1,
    'disable_existing_loggers' : False,
    'handlers' : {
        'file' : {
            'class' : 'logging.FileHandler',
            'level' : 'DEBUG',
            'filename' : 'debug.log',
        },
    },
    'loggers': {
        'django' : {
            'handlers' : ['file'],
            'level' : 'INFO',
            'propagate' : True
        }
        
    }
} 


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES' : [
        'main.api.backends.JWTAuthentication',
    ],
    'EXCEPTIONS_HANDLER' : 'project.exceptions.core_exception_handler',
    'NON_FIELD_ERRORS_KEY' : 'message',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware' , 
    'django.middleware.common.CommonMiddleware', 
]

CORS_ALLOW_ORIGINS = get_setting('CORS_ALLOW_ORIGINS')

ROOT_URLCONF = 'backPython.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'client/build'],
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

WSGI_APPLICATION = 'backPython.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = { 
    'default': {
        'ENGINE': get_setting('ENGINE'),
        'NAME': get_setting('NAME'),
        'USER': get_setting("USER"),
        'PASSWORD': get_setting('PASSWORD'),
        'HOST' : get_setting('HOST'),
        'PORT' : get_setting('PORT'),
    },
    # 'default': {
        # 'ENGINE' : 'django.db.backends.sqlite3',
        # 'NAME' : 'test_db'
    # }
}

AUTH_USER_MODEL = "main.User"

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = (
    (BASE_DIR / 'client/build/static'),
)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
