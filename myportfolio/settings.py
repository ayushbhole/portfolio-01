from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# --- 1. SECURITY & HOSTS ---
SECRET_KEY = os.environ.get('SECRET_KEY', 'default-key-for-local-dev-only-change-this')
DEBUG = os.environ.get('DJANGO_DEBUG') == 'False' 

# CRITICAL: Allows Vercel's domain for deployment
ALLOWED_HOSTS = [
    '127.0.0.1', 
    'localhost', 
    '.vercel.app', 
    'portfolio-sepia-two-11.vercel.app' 
]

# --- 2. APPS & MIDDLEWARE ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'tailwind',
    'theme',
    'captcha',
    'myportfolio',
    'widget_tweaks',
]

# MIDDLEWARE = [
#     # CRITICAL: WhiteNoise MUST be listed directly after SecurityMiddleware.
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware', 
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

ROOT_URLCONF = 'myportfolio.urls'
WSGI_APPLICATION = 'myportfolio.wsgi.application'

# # --- 3. STATIC FILES (The Final Fix) ---
# STATIC_URL = '/static/' 

# # Tells collectstatic where your root 'static' folder is located.
# STATICFILES_DIRS = [
#     BASE_DIR / 'static', 
# ]

# # Where collectstatic puts ALL files (must match vercel.json)
# STATIC_ROOT = BASE_DIR / "staticfiles_build" 

# # FINAL FIX: Simplified WhiteNoise storage (bypasses complex manifest lookup)
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
# import os
# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / "static"]
# STATIC_ROOT = BASE_DIR / "staticfiles_build"
# STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


# This is the URL browsers request
STATIC_URL = 'static/'
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles_build','static')

 

# settings.py

TEMPLATES = [
    {
        # CRITICAL FIX: The required template engine definition is missing
        'BACKEND': 'django.template.backends.django.DjangoTemplates', 
        
        # This points to your root-level 'templates' folder
        'DIRS': [BASE_DIR / 'templates'], 
        
        # This tells Django to look for templates inside each installed app's 'templates' folder
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

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



import dj_database_url 

# ... other settings ...

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
       
    )
}

# Fallback for local development using sqlite (optional)
if 'DATABASE_URL' not in os.environ and 'default' not in DATABASES:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }


# # --- 4. ETC (Database, Email, Timezone) ---
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'