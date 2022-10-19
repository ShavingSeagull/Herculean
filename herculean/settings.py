import os
#import env
import dj_database_url

if os.getenv('BUILD_ON_TRAVIS', None):
    SECRET_KEY = "SecretKeyForUseOnTravis"
else:
    SECRET_KEY = os.environ.get("SECRET_KEY")

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'DEV' in os.environ

ALLOWED_HOSTS = ['127.0.0.1', 'herculean-store.herokuapp.com', 'herculean-store.onrender.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_forms_bootstrap',
    'django_gravatar',
    'disqus',
    'home',
    'contact',
    'accounts',
    'news',
    'products',
    'profiles',
    'reviews',
    'promocodes',
    'cart',
    'checkout',
    'storages',
]

DISQUS_API_KEY = os.environ.get("DISQUS_API_KEY")
DISQUS_WEBSITE_SHORTNAME = 'herculean'
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'herculean.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'cart.contexts.cart_contents',
            ],
        },
    },
]

WSGI_APPLICATION = 'herculean.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

if "DATABASE_URL" in os.environ:
    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
else:
    print("Database URL not found. Using SQLite.")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.CaseInsensitiveAuth'
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

DATETIME_FORMAT = 'd-m-Y'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
AWS_STORAGE_BUCKET_NAME = 'herculean-store'
AWS_S3_REGION_NAME = 'us-east-2'
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

STRIPE_PUBLISHABLE = os.environ.get("STRIPE_PUBLISHABLE")
STRIPE_SECRET = os.environ.get("STRIPE_SECRET")

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'accounts@herculean.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_PORT = 1025
