from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import EmailField
from wtforms import validators

class ProfesorForm(Form):
    id = IntegerField('Id')
    nombre = StringField('Nombre')
    apellidos = StringField('Apellidos')
    email = EmailField('Correo Electronico')
    especialidad = StringField('Especialidad Profesor')
    sueldo = StringField('Sueldo')