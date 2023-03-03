from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Alumnos(db.Model):
    __tablename__ = 'alumno'
    id = db.Column(db.Integer, primary_key = True) # El true funciona para que sea autoincrementable
    nombre = db.Column(db.String(50))
    apellidos = db.Column(db.String(100)) #Parametros para crear los varchar
    email = db.Column(db.String(50))
    create_date = db.Column(db.DateTime, default = datetime.datetime.now) # esto nos ayudara a poner la hora y fecha actual