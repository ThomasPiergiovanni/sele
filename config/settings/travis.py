import os
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
os.environ['GDAL_DATA'] = r"/home/travis/virtualenv/python3.9.12/lib/python3.9/site-packages/osgeo/data/gdal"
os.environ['PROJ_LIB'] = r"/home/travis/virtualenv/python3.9.12/lib/python3.9/site-packages/osgeo/data/proj"
os.environ['PATH'] = r"/home/travis/virtualenv/python3.9.12/lib/python3.9/site-packages/osgeo" +";" + os.environ['PATH']
GDAL_LIBRARY_PATH = r"/home/travis/virtualenv/python3.9.12/lib/python3.9/site-packages/osgeo/gdal304.dll"