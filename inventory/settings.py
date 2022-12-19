import environ
import os
from datetime import timedelta
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# False if not in os.environ because of casting above
DEBUG = env('DEBUG')

# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = ['*']

CRISPY_TEMPLATE_PACK = 'bootstrap5'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # local
    'accounts.apps.AccountsConfig',
    'backend',
    'widget_tweaks',
    'crispy_forms',
    ## Restframework API
    'rest_framework',
    'djoser',
    # Templates
    'bootstrap4',
    'bootstrap_datepicker_plus',
    # Third party app
    "phonenumber_field",
    'drf_yasg',

]

AUTH_USER_MODEL='accounts.User'

REST_FRAMEWORK={
    'NON_FIELD_ERRORS_KEY':'errors',
     'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'rest_framework_simplejwt.tokens.AccessToken',
    ),
}
SIMPLE_JWT={
    'AUTH_HEADER_TYPES':('Bearer',),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),

}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer':{
            'type':'apiKey',
            'name':'Authorization',
            'in':'header'
     }
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'inventory.urls'
AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.RemoteUserBackend',
        'django.contrib.auth.backends.ModelBackend',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR ,'accounts','templates')],
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

WSGI_APPLICATION = 'inventory.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'mydatabase', # This is where you put the name of the db file. 
#                  # If one doesn't exist, it will be created at migration time.
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'solidality',
        'USER':'postgres',
        'PASSWORD':'rutre',
        'HOST':'localhost',
        'PORT':5432
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_ROOT= os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'inventory/static')
]


# DEFAULT VALUE

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
