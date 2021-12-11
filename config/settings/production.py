from . import *

SECRET_KEY = '-~aO;| F;rE[??/w^ztrmh(9'
DEBUG = False
ALLOWED_HOSTS = ['165.232.84.118', 'localhost']

DATABASES = {
    'default': {
        # on utilise l'adaptateur postgresql
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sele_db',  # le nom de notre base de données créée précédemment
        'USER': 'thomasadmin',  # attention : remplacez par votre nom d'utilisateur !!
        'PASSWORD': 'SelE$2021!!',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
