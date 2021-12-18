import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENV = 'test'
ENV_SECRET_KEY = 'django-insecure-+f^i^1jx+g5*k$2a13t)^x-0b6$2@nbgd8v$ggufbyh62h*)gc'
ENV_DEBUG = True
ENV_ALLOWED_HOSTS = []
ENV_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sele_db',  # le nom de notre base de données créée précédemment
        'USER': 'postgres',  # attention : remplacez par votre nom d'utilisateur !!
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
ENV_SECURE_SSL_REDIRECT = False
ENV_SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ENV_STATIC_URL = '/static/'
ENV_STATIC_ROOT = None

