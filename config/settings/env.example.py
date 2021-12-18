ENV = 'test'
SECRET_KEY = 'django-insecure-+f^i^1jx+g5*k$2a13t)^x-0b6$2@nbgd8v$ggufbyh62h*)gc'
DEBUG = True
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sele_db',  # le nom de notre base de données créée précédemment
        'USER': 'postgres',  # attention : remplacez par votre nom d'utilisateur !!
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
STATIC_URL = '/static/'
STATIC_ROOT = None
