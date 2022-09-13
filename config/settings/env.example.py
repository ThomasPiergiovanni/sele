import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_GDAL_DATA = r"D:\projects\sele\env\Lib\site-packages\osgeo\data\gdal"
ENV_PROJ_LIB = r"D:\projects\sele\env\Lib\site-packages\osgeo\data\proj"
ENV_PATH= r"D:\projects\sele\env\Lib\site-packages\osgeo" +";" + os.environ['PATH']
ENV_GDAL_LIBRARY_PATH = r'D:\projects\sele\env\Lib\site-packages\osgeo\gdal304.dll'
ENV_SECRET_KEY = 'django-insecure-+f^i^1jx+g5*k$2a13t)^x-0b6$2@nbgd8v$ggufbyh62h*)gc'
ENV_DEBUG = False
ENV_ALLOWED_HOSTS = []
ENV_DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'xxxxx', 
        'USER': 'xxxxx',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
ENV_SECURE_SSL_REDIRECT = True
ENV_SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ENV_STATIC_URL = '/static/'
ENV_STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
ENV_MAPBOX_TOKEN= 'xxxxxx'

