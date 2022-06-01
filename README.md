# sel-e - système d'échange local - électronique (Electronic local exchange system).

## 1. Introduction.

This program is named "sel-e". It's an electronic local exchange system that fit into the perspective of an alternative to the current economic system.

The web app backend is built with Django framework. The frontend uses mainly a template Dashboard provided by AdminLTE built with Bootstrap/Javascipt. The programm is hosted by Digital Ocean.

You can check it app on  [(https://sel-e.fr](https://sel-e.fr)

The here below installation steps describes how to make the install on a dev and local environment.

NB: It's a programm written in the context of a Django app eductation module delivered by [OpenClassRooms](https://openclassrooms.com).

## 2. Prerequisite.

This program requires the following components:
* Python 3.8.10
* PostgreSQL 12.11
* PostgresSQL 12 Postgis extension
* GDAL library 3.4.1

The others required program will be installed via pip using requirements.txt file (see further).

## 3. Installation.

These instructions are for deployment on a local machine i.e. for development use. It's described for install on a Windows OS. Installing on another OS might vary.

### 3.1. Download.
Download/clone this repository on your system, at the location that suits you best.
> git clone https://github.com/ThomasPiergiovanni/sele.git

### 3.2. Python 3 install.
Make sure you have Python 3 installed.
> python --version

If not, you can download it and install it from the [python official website](https://www.python.org/). You will find the necessary documentation there.

### 3.3. PostgreSQL 13 install and start.
Make sure you have PostgreSQL 12 installed.
> psql --version

If not, you can download it and install it from the [postgresql official website](https://www.postgresql.org/download/). You will find the necessary documentation there.

### 3.4. Create DB.
Create database.
> createdb -h localhost -p 5432 -U yourusername yourdatabasename

### 3.5. Create Postgis extension.
 and Create Postgis extensiion.

1. Connect to the created database.
    > psql -U yourusername -d yourdatabasename

2. Create Postgis extension.
    > yourdatabasename=# CREATE POSTGIS;

Notes: 
  * You need superuser privileges to execute this command.
    > ALTER ROLE <user_name> SUPERUSER;

  * On Linux OS you'll probably need to install first the postgis_extension_script first prior to execute the Postgis instruction.
    > sudo apt install postgresql-12-postgis-scripts

### 3.6. Intsall GDAL library.

You need to insatll GDAL library. The proposed intall here uses .whl file.

1. On Windows OS, download GDAL .whl on [unofficial Windows Binairies for Pythob Extension Packages by Christop Gohlke, University of California website](https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal) and choose the version that suits your OS and Python versions.

Note: on Linux OS, download GDAL .whl on [https://sourceforge.net](https://sourceforge.net/projects/gdal-wheels-for-linux/files/) and choose the version that suits your OS and Python versions.

2. Install the GDAL.whl
    > pip install GDAL-3.4.1-cp38-cp38-win_amd64.whl

### 3.7. Create & activate a virtual environment (recommended).

1. Go at the app "root" repository.
    > cd yourpath\sele

2. Create a virtual environment using venv package.
    > python -m venv env

3. Activate the virtual environment.
    > env/scripts/activate

Documentation is also available on the [python official website](https://www.python.org/).

### 3.8. Django and other programms install.
Install Django and the others programs on you virtual environment using the requirements.txt file.
>pip install -r requirements.txt

Please refer to [Django documentation](https://docs.djangoproject.com/fr/3.1/) for more information.

Note: On Linux OS you might also need to install the following packages:
> sudo apt install numpy, GDAL

### 3.9. Application mandatory settings.
1. Change constants with the appropriate value into **config/settings.py/__init__.py** :
* ENV = Depending on the environnement, set the appropriate value ('test', 'staging', 'production').

If your environnement is 'test' set the appropriate value into **config/settings.py/testing_env.py**

* BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
* TENV_GDAL_DATA = r"\yourpath\sele\env\Lib\site-packages\osgeo\data\gdal"
* TENV_PROJ_LIB = r"\yourpath\sele\env\Lib\site-packages\osgeo\data\proj"
* TENV_PATH= r"\yourpath\sele\env\Lib\site-packages\osgeo" +";" + os.environ['PATH']
* TENV_GDAL_LIBRARY_PATH = r'\yourpath\sele\env\Lib\site-packages\osgeo\gdal304.dll'
* TENV_SECRET_KEY = 'django-insecure-+f^i^1jx+g5*k$2a13t)^x-0b6$2@nbgd8v$ggufbyh62h*)gc'
* TENV_DEBUG = True
* TENV_ALLOWED_HOSTS = []
* TENV_DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'sele_db',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }

* TENV_SECURE_SSL_REDIRECT = False
* TENV_STATIC_URL = '/static/'
* TENV_STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
* TENV_MAPBOX_TOKEN = ''

Aditionnaly, if your environnement is 'staging' and you use Travis for CI, set the approrpiate value into that same  **config/settings.py/testing_env.py**
**config/settings.py/testing_env.py**

* SENV_GDAL_DATA = r"/home/travis/virtualenv/python3.9.12/lib/python3.9/site-packages/osgeo/data/gdal"
* SENV_PROJ_LIB = r"/home/travis/virtualenv/python3.9.12/lib/python3.9/site-packages/osgeo/data/proj"
* SENV_PATH = r"/home/travis/virtualenv/python3.9.12/lib/python3.9/site-packages/osgeo" +";" + os.environ['PATH']
* SENV_GDAL_LIBRARY_PATH = r"/home/travis/virtualenv/python3.9.12/lib/python3.9/site-packages/osgeo/lib/libgdal.so"

Finally if your environnement is 'production', rename file **config/settings.py/env.example.py** into **env.py** and set the approrpiate value into that renamed **config/settings.py/env.py**

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_GDAL_DATA = r"\yourpath\sele\env\Lib\site-packages\osgeo\data\gdal"
ENV_PROJ_LIB = r"\yourpath\sele\env\Lib\site-packages\osgeo\data\proj"
ENV_PATH= r"\yourpath\sele\env\Lib\site-packages\osgeo" +";" + os.environ['PATH']
ENV_GDAL_LIBRARY_PATH = r'\yourpath\sele\env\Lib\site-packages\osgeo\gdal304.dll'
ENV_SECRET_KEY = 'xxxxx'
ENV_DEBUG = False
ENV_ALLOWED_HOSTS = [xxx.xxx.xxx]
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
ENV_MAPBOX_TOKEN= 'xxxxxx'. 

You can check section **4. Settings** for description of these constants.

### 3.10. Apply DB migrations.
Run migration to setup the DB correctly.
> python manage.py migrate


### (Optionnal) 3.11. Collectatic.
On a production environnement on Linux OS, you'll also need to collect static files.
> python manage.py collectstatic

### 3.12. Start the program.
All install steps are completed for dev environnment install. You can start teh app with the following command.
> python manage.py runserver

### 3.13. Test the program.
If you want to perform test after having modified the code, you can run tests.
> python manage.py test

### 3.12. Deactivate the virtual environment.
Once you're done using the program, you should leave the virtual environment. Simply type the following statement in your bash.
> deactivate

### 3.13. Uninstall.
If you want to uninstall the program, simply delete the complete repository form your device.