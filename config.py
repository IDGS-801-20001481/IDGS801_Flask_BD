import os

from sqlalchemy import create_engine
from decouple import config

import urllib
import pymysql

class Config(object):
    SECRET_KEY = 'MY_SECRET_KEY'
    SESSION_COOKIE_SECURE = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:cordova@127.0.0.1/idgs801'
    SQLALCHEMY_TRACK_MODIFICATION = False
    