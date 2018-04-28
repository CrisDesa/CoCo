# archivo de configuracion
import os


# configuracion para modulo Flask-WTF
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'oracle://conocer:conocer@192.168.1.5:1528/DSBC'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
