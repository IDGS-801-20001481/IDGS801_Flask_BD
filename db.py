import os
from decouple import config
import pymysql


def get_conexion():
    conn = pymysql.connect(
        host=config('MYSQL_HOST'),
        user=config('MYSQL_USER'),
        password=config('MYSQL_PASS'),
        database=config('MYSQL_DB'),
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn
    