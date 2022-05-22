from . import *

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'sele_db',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}
TENV_GDAL_DATA = r"/home/travis/virtualenv/python3.9.12/lib/python3.9/site-packages/osgeo/data/gdal"
TENV_PROJ_LIB = r"/home/travis/virtualenv/python3.9.12/lib/python3.9/site-packages/osgeo/data/proj"
TENV_PATH= r"/home/travis/virtualenv/python3.9.12/lib/python3.9/site-packages/osgeo" +";" + os.environ['PATH']
TENV_GDAL_LIBRARY_PATH = r'/home/travis/virtualenv/python3.9.12/lib/python3.9/site-packages/osgeo/gdal304.dll'