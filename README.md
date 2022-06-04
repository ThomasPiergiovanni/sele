# sel-e: système d'échange local électronique (electronic local exchange trading system).

## 1. Introduction.

This program is named **sel-e**. It stands for *"système d'échange local électronique"* i.e. *"electronic local exchange trading system"*. *sel-e* fits into the perspective of an alternative to the current economic system. It's a trading web application of non-monetized goods and services carried out within the perimeter of a municipality.

Wikipedia definition of *local exchange trading system* is the following : *"A local exchange trading system (also local employment and trading system or local energy transfer system; abbreviated LETS) is a locally initiated, democratically organised, not-for-profit community enterprise that provides a community information service and records transactions of members exchanging goods and services by using locally created currency.[1] LETS allow people to negotiate the value of their own hours or services,[2] and to keep wealth in the locality where it is created"*.

The web app backend is built in Python with Django framework. The frontend uses mainly a template Dashboard provided by AdminLTE built with Bootstrap/JavaScript. The programm is hosted by Digital Ocean.

You can check it app on  [https://sel-e.fr](https://sel-e.fr).

The here below installation steps describes how to make the install on a dev and local environment.

NB: This programm is written in the context of a Django app eductation module delivered by [OpenClassRooms](https://openclassrooms.com).

## 2. Prerequisite.

This program requires the following components:
* Python 3.8.10
* PostgreSQL 12.11
* PostgresSQL 12 Postgis extension
* GDAL library 3.4.1

The others required program will be installed via pip using requirements.txt file (see further).

## 3. Installation.

These instructions are for deployment on a local machine i.e. for development use. It's described for install on a Windows OS. Some notes are also provided for installing on Linux but the full install steps are not provided.

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
Create Postgis extensiion.

1. Connect to the created database.
    > psql -U yourusername -d yourdatabasename

2. Create Postgis extension.
    > yourdatabasename=# CREATE POSTGIS;

Notes: 
  * You need superuser privileges to execute *CREATE POSTGIS* command.
    > ALTER ROLE <user_name> SUPERUSER;

  * On Linux, you'll probably need to install *postgis_extension_script* prior to execute the *CREATE POSTGIS* instruction.
    > sudo apt install postgresql-12-postgis-scripts

### 3.6. Install GDAL library.

You need to install GDAL library. The proposed intsall here uses .whl file.

1. Download GDAL .whl from [https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal](https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal) provided by **Christop Gohlke, University of California** and choose the version that suits your OS and Python versions.


2. Install the GDAL.whl
    > pip install GDAL-3.4.1-cp38-cp38-win_amd64.whl


Note: on Linux, download GDAL .whl on [https://sourceforge.net](https://sourceforge.net/projects/gdal-wheels-for-linux/files/) and choose the version that suits your OS and Python versions. If the OS don't handle .whl, consider usiong *apt* to get GDAL (and numpy...seems required).
> sudo apt install numpy, GDAL

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
Check section **4. Settings** for description of the followings variables.

#### 3.9.1. **config/settings.py/__init__.py**. .
Change variable with the appropriate values.   

* ENV = 'test'

#### 3.9.2. **config/settings.py/testing_env.py**.

##### 3.9.2.1. 'test'.
If your environnement is 'staging', change variables with the appropriate values.  


* BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
* TENV_GDAL_DATA = r"\yourpath\sele\env\Lib\site-packages\osgeo\data\gdal"
* TENV_PROJ_LIB = r"\yourpath\sele\env\Lib\site-packages\osgeo\data\proj"
* TENV_PATH= r"\yourpath\sele\env\Lib\site-packages\osgeo" +";" + os.environ['PATH']
* TENV_GDAL_LIBRARY_PATH = r'\yourpath\sele\env\Lib\site-packages\osgeo\gdal304.dll'
* TENV_SECRET_KEY = 'django-insecure-+f^i^1jx+g5*k$2a13t)^x-0b6$2@nbgd8v$ggufbyh62h)gc'
* TENV_DEBUG = True
* TENV_ALLOWED_HOSTS = []
* TENV_DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'xxxxx',
            'USER': 'xxxxx',
            'PASSWORD': 'xxxxx',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }

* TENV_SECURE_SSL_REDIRECT = False
* TENV_STATIC_URL = '/static/'
* TENV_STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
* TENV_MAPBOX_TOKEN = ''

##### 3.9.2.2. 'staging'.
If your environnement is 'staging' and you use Travis for CI, change variables with the appropriate values.

* SENV_GDAL_DATA = r"/home/travis/virtualenv/python3.9.12/lib/python3.9/site-packages/osgeo/data/gdal"
* SENV_PROJ_LIB = r"/home/travis/virtualenv/python3.9.12/lib/python3.9/site-packages/osgeo/data/proj"
* SENV_PATH = r"/home/travis/virtualenv/python3.9.12/lib/python3.9/site-packages/osgeo" +";" + os.environ['PATH']
* SENV_GDAL_LIBRARY_PATH = r"/home/travis/virtualenv/python3.9.12/lib/python3.9/site-packages/osgeo/lib/libgdal.so"

#### 3.9.3. **config/settings.py/env.example.py**
If your environnement is 'production', rename file **config/settings.py/env.example.py** into **env.py** and change variables with the appropriate value into that renamed file.  

* BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
* ENV_GDAL_DATA = r"\yourpath\sele\env\Lib\site-packages\osgeo\data\gdal"
* ENV_PROJ_LIB = r"\yourpath\sele\env\Lib\site-packages\osgeo\data\proj"
* ENV_PATH= r"\yourpath\sele\env\Lib\site-packages\osgeo" +";" + os.environ['PATH']
* ENV_GDAL_LIBRARY_PATH = r'\yourpath\sele\env\Lib\site-packages\osgeo\gdal304.dll'
* ENV_SECRET_KEY = 'xxxxx'
* ENV_DEBUG = False
* ENV_ALLOWED_HOSTS = [xxx.xxx.xxx]
* ENV_DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'xxxxx', 
        'USER': 'xxxxx',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
* ENV_SECURE_SSL_REDIRECT = True
* ENV_SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
* ENV_STATIC_URL = '/static/'
* ENV_STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
* ENV_MAPBOX_TOKEN= 'xxxxxx'

### 3.10. Apply DB migrations.
Run migration to setup the DB correctly.
> python manage.py migrate


### 3.11. Collectatic (production env only).
On a production environnement, you'll also need to collect static files.
> python manage.py collectstatic

### 3.12. Start the program.
All install steps are completed for dev environnment install. You can start teh app with the following command.
> python manage.py runserver

### 3.14. Test the program.
If you want to perform test after having modified the code, you can run tests.
> python manage.py test

### 3.15. Deactivate the virtual environment.
Once you're done using the program, you should leave the virtual environment. Simply type the following statement in your bash.
> deactivate

### 3.16. Uninstall.
If you want to uninstall the program, simply delete the complete repository form your device.

## 4. Settings.
As mentionned in section *3.9. Application mandatory settings*, changing settings **must be** done in *config/settings.py/__init__.py*
and, depending on you environnement, also in  *config/settings.py/testing_env.py* and in
*config/settings.py/env.py (from renamed config/settings.py/env.example.py)*.  

**Make sure to read section *"3.9. Application mandatory settings"* to proceed correctly.**



### 4.1. config/settings.py/__init__.py
#### 4.1.1. ENV.
DESCRIPTION: Environnment variable. Defines the environnement in which the programm is deployed.  
MANDATORY: Yes.  
DEFAULT SETTINGS: 'test'.  
CUSTOM SETTINGS: Value can either be set to *'test'*, *'staging'*, *'production'* depending your deploying environnement.

### 4.2. config/settings.py/testing_env.py
#### 4.2.1. BASE_DIR.
DESCRIPTION: BASE_DIR points to top hierarchy of the project i.e. sele, All paths defined are all relative to BASE_DIR.  
MANDATORY: Yes.    
DEFAULT SETTINGS: os.path.dirname(os.path.dirname(os.path.abspath(__file__))).    
CUSTOM SETTINGS: No.  

#### 4.2.2. TENV_GDAL_DATA.
DESCRIPTION:  Environmental variable 'GDAL_DATA' (os.environ['GDAL_DATA'])value. It's the path to gdal data module.  
MANDATORY: Yes.   
DEFAULT SETTINGS: r"D:\02_oc\13_P13\env\Lib\site-packages\osgeo\data\gdal".   
CUSTOM SETTINGS: Yes. Must be set according to the app path i.e.  r"\pathtotheapp\sele\env\Lib\site-packages\osgeo\data\gdal".

#### 4.2.3. TENV_PROJ_LIB.
DESCRIPTION:  Environmental variable 'PROJ_LIB' (os.environ['PROJ_LIB'])value. It's the path to proj lib module.  
MANDATORY: Yes.   
DEFAULT SETTINGS: r"D:\02_oc\13_P13\env\Lib\site-packages\osgeo\data\proj".    
CUSTOM SETTINGS: Yes. Must be set according to the app path i.e. r"\pathtotheapp\sele\env\Lib\site-packages\osgeo\data\proj".  

#### 4.2.4. TENV_PATH.
DESCRIPTION: Environmental variable 'PATH' (os.environ['PATH']) value. It's the path to osgeo module.  
MANDATORY: Yes.   
DEFAULT SETTINGS: r"D:\02_oc\13_P13\env\Lib\site-packages\osgeo" +";" + os.environ['PATH'].  
CUSTOM SETTINGS: Yes. Must be set according to the app path i.e. r"\pathtotheapp\sele\env\Lib\site-packages\osgeo" +";" + os.environ['PATH'].  

#### 4.2.5. TENV_GDAL_LIBRARY_PATH.
DESCRIPTION: Path variable to the gdal library'.  
MANDATORY: Yes.  
DEFAULT SETTINGS: r'D:\02_oc\13_P13\env\Lib\site-packages\osgeo\gdal304.dll'.  
CUSTOM SETTINGS: Yes. Must be set according to the app path i.e. r"\pathtotheapp\sele\env\Lib\site-packages\osgeo\gdal304.dll'.  

#### 4.2.6. SENV_GDAL_DATA.
DESCRIPTION: Same as TENV_GDAL_DATA but for continuous integration in a Linux OS. Environmental variable 'GDAL_DATA' (os.environ['GDAL_DATA'])value. It's the path to gdal data module.  
MANDATORY: No. Required only if planning continuous integration with Travis.  
DEFAULT SETTINGS: r"/home/travis/virtualenv/python3.9.12/lib/python3.9/site-packages/osgeo/data/gdal".   
CUSTOM SETTINGS: Yes. Must be set according to the app path i.e. r"\pathtotheapp\sele\env\Lib\site-packages\osgeo\data\gdal".  

#### 4.2.7. SENV_PROJ_LIB.
DESCRIPTION: Same as TENV_PROJ_LIB but for continuous integration in a Linux OS. Environmental variable 'PROJ_LIB' (os.environ['PROJ_LIB']) value. It's the path to proj lib module.  
MANDATORY: No. Required only if planning continuous integration with Travis.  
DEFAULT SETTINGS: r"/home/travis/virtualenv/python3.9.12/lib/python3.9/site-packages/osgeo/data/proj".   
CUSTOM SETTINGS: Yes. Must be set according to the app path i.e. r"\pathtotheapp\sele\env\Lib\site-packages\osgeo\data\proj".  

#### 4.2.8. SENV_PATH.
DESCRIPTION:  Same as TENV_PATH but for continuous integration in a Linux OS. Environmental variable 'PATH' () os.environ['PATH'] value. It's the path to osgeo module.  
MANDATORY:  No. Required only if planning continuous integration with Travis.    
DEFAULT SETTINGS: r"/home/travis/virtualenv/python3.9.12/lib/python3.9/site-packages/osgeo" +";" + os.environ['PATH'].  
CUSTOM SETTINGS: Yes. Must be set according to the app path i.e. r"\pathtotheapp\sele\env\Lib\site-packages\osgeo" +";" + os.environ['PATH'].  

#### 4.2.9. SENV_GDAL_LIBRARY_PATH.
DESCRIPTION:  Same as TENV_GDAL_LIBRARY_PATH but for continuous integration in a Linux OS. Path variable to the gdal library'.  
MANDATORY:  No. Required only if planning continuous integration with Travis.    
DEFAULT SETTINGS: r"/home/travis/virtualenv/python3.9.12/lib/python3.9/site-packages/osgeo/lib/libgdal.so".  
CUSTOM SETTINGS: Yes. Must be set according to the app path i.e. r"\pathtotheapp\sele\env\Lib\site-packages\osgeo\gdal304.dll'.   

#### 4.2.10. TENV_SECRET_KEY.
DESCRIPTION:  Application secret key.  
MANDATORY:  Yes.    
DEFAULT SETTINGS: "xxxxxx"  
CUSTOM SETTINGS: Yes.  

#### 4.2.11. TENV_DEBUG.
DESCRIPTION:  Defines if the app is in debug mode or not.  
MANDATORY:  Yes.    
DEFAULT SETTINGS: True.  
CUSTOM SETTINGS: Either True or False. Never use True in a production environnement.  

#### 4.2.12. TENV_ALLOWED_HOSTS.
DESCRIPTION:  List of allowed IP.  
MANDATORY:  No. Required when deploying app on a server.  
DEFAULT SETTINGS: [].  
CUSTOM SETTINGS: Enter the differents allowed IP e.g. [190.325.65.211, www.myapp.whatever].  

#### 4.2.13. TENV_DATABASES.
DESCRIPTION:  PostgreSQL/PostGIS database settings.  
MANDATORY:  Yes.  
DEFAULT SETTINGS: {  
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'db_name',
        'USER': 'user_name',
        'PASSWORD': 'pwd',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}.  
CUSTOM SETTINGS: NAME, USER, PASSWORD must be set according to your database configuration. See section 3.4.  

#### 4.2.14. TENV_SECURE_SSL_REDIRECT.
DESCRIPTION:  Boolean defining to redirect every http request to HTTPS.  
MANDATORY:  Yes.  
DEFAULT SETTINGS: False.  
CUSTOM SETTINGS: Value can either be False or True.  

#### 4.2.15. TENV_STATIC_ROOT.
DESCRIPTION:  The absolute path to the directory where collectstatic will collect static files for deployment.  
MANDATORY:  Yes.  
DEFAULT SETTINGS: os.path.join(BASE_DIR, 'static/').  
CUSTOM SETTINGS: Can be changed to any empty directory. Not remomended though.  

#### 4.2.16. TENV_STATIC_URL.
DESCRIPTION:  URL to use when referring to static files located in STATIC_ROOT.  
MANDATORY:  Yes.  
DEFAULT SETTINGS: '/static/'.  
CUSTOM SETTINGS: Can be changed to any name, url. Not remomended though.  

#### 4.2.17. TENV_MAPBOX_TOKEN.
DESCRIPTION:  MapBox Token necessary to diplay a map background. A map background must be created and its token created. Check at [MapBox](https://www.mapbox.com/).  
MANDATORY:  No.  
DEFAULT SETTINGS: 'xxxxxx'    
CUSTOM SETTINGS: It need to be set.  

### 4.3. config/settings.py/env.py (from renamed config/settings.py/env.example.py)
#### 4.3.1. BASE_DIR.
Same as *"4.2.1 BASE DIR"*.

#### 4.3.2. ENV_GDAL_DATA.
Same as *"4.2.2. TENV_GDAL_DATA"*.

#### 4.3.3. ENV_PROJ_LIB.
Same as *"4.2.3. TENV_PROJ_LIB"*.

#### 4.3.4. ENV_PATH.
Same as *"4.2.4. TENV_PATH"*.

#### 4.3.5. ENV_GDAL_LIBRARY_PATH.
Same as *"4.2.5. TENV_GDAL_LIBRARY_PATH"*. 

#### 4.3.6. ENV_SECRET_KEY.
Same as *"4.2.10. TENV_SECRET_KEY"*.  

#### 4.3.7. ENV_DEBUG.
Same as *"4.2.11. TENV_DEBUG"*.   

#### 4.3.8. ENV_ALLOWED_HOSTS.
Same as *"4.2.12. TENV_ALLOWED_HOSTS"*.   

#### 4.3.9. ENV_ALLOWED_HOSTS.
Same as *"4.2.13. TENV_ALLOWED_HOSTS"*. 

#### 4.3.10. ENV_SECURE_SSL_REDIRECT.
Same as *"4.2.14. TENV_SECURE_SSL_REDIRECT"*. 

#### 4.3.11. ENV_STATIC_ROOT.
Same as *"4.2.15. TENV_STATIC_ROOT"*.

#### 4.3.12. ENV_STATIC_ROOT.
Same as *"4.2.16. TENV_STATIC_ROOT"*.

#### 4.3.13. ENV_MAPBOX_TOKEN.
Same as *"4.2.17. TENV_MAPBOX_TOKEN"*. but with MANDATORY = True.

## 5. Users' guide.

### 5.1. Program functionalities
The program provides the following functionalities:
1. Create account
2. login.
3. Make proposition (offer and demand).
4. Select propositions and execute them.
5. Comment a proposition.
6. Create discussion.
7. Make comments into a discussion.
8. Create votation.
9. Vote in a votation.

### 5.2. How to.
* Browse to the app url i.e. http://127.0.0.1:8000/ (on the dev environment) or https://sel-e.fr/ (official release). You can find instruction on how to use it on the **About page**. The main functionnalities are however described here.

#### 5.2.1. Sign up
Provide email, password, username postal code and city name to create an account. "Proposition" can only be made in your belonging city.

#### 5.2.2. Proposition
Propsoition module allow exchanges. Propositions are of two types: Offer and Demands.

A member (signed-in user) can make or repsond to Offer and Demand. At each stage of the Proposition, members  involved in the proposition ("creator" and "taker"), update the Proposition's status in order to report on the Proposition's progression.

Each Proposition ariving at its end i.e. when a "job" is achieved and validated by the "beneficiary", the defined "time of execution" mentionned originally in the proposition by the "creator" is  credited to the "performer" "time wallet" and debited to the "beneficiary" one.

Note that Proposition of type Demand can be made on behalfs of the collectivity. In that case all "beneficiaries" i.e. all members of the collectivity are debited once the Proposition is completed. Proposition of Type Demand can be defined Collective at the Proposition creation by filling the field "Portée" with value "Collective". The modules Discussion and Votation allow members to discuss and decide when and for what making Collective Demand.

#### 5.2.3. Discussion
Discussion module allow members of a same Collectivity to create Discussions and to exchange with the chat. It's main purpose is to allow discussion for making Collective Demands.

#### 5.2.4. Votation
Votation module allow members of a same Collectivity to create Votation and to vote on the Votation subject. It's main purpose is to allow the Collectivity to create Votation for deciding on Collective Demands.