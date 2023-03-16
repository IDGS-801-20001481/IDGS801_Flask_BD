from flask import Blueprint
from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
from Controladores.controller_profesores import *
from pprint import pprint
from datetime import datetime


from Profesores import Profesor


profesores = Blueprint('profesores', __name__, template_folder='templates')

@profesores.route('/get_all', methods=['GET', 'POST'])
def get_all_profesores():
    create_form = Profesor.ProfesorForm(request.form)
    profesores = get_all()
    pprint(profesores)

    if request.method == 'POST':
        word = create_form.id.data 
        if not word:  # Si el formulario está vacío, devuelve todos los profesores
            profesores = get_all()
        else:
            profesores = search(word)

    return render_template("profesores.html", form=create_form, profesores=profesores)

@profesores.route('/search', methods=['GET', 'POST'])
def get_all_id():
    create_form = Profesor.ProfesorForm(request.form)
    profesores = get_all()
    pprint(profesores)

    if request.method == 'POST':
        word = create_form.id.data 
        if(word == None):
            word = create_form.nombre.data 
            
        if not word:  # Si el formulario está vacío, devuelve todos los profesores
            profesores = get_all()
        else:
            profesores = search(word)

    return render_template("profesores.html", form=create_form, profesores=profesores)


@profesores.route('/insert', methods=['GET', 'POST'])
def insert_profesores():
    create_form = Profesor.ProfesorForm(request.form)
    nombre = create_form.nombre.data
    apellidos = create_form.apellidos.data
    email = create_form.email.data
    especialidad = create_form.especialidad.data
    sueldo = create_form.sueldo.data
    ok = ""
    if request.method=='POST':
        ok = insert(nombre, apellidos, email, especialidad, sueldo)
    return render_template("insert.html", form=create_form, insert_prof=insert, ok = ok)


@profesores.route('/update', methods=['GET', 'POST'])
def update_profesores():
    
    create_form = Profesor.ProfesorForm(request.form)
    ok = None
    if request.method=='GET':
        id=int(request.args.get('id'))
        profesor = search(id)
        create_form.id.data = id
        create_form.nombre.data = profesor[0]['nombre']
        create_form.apellidos.data = profesor[0]['apellidos']
        create_form.email.data = profesor[0]['email']
        create_form.especialidad.data = profesor[0]['especialidad']
        create_form.sueldo.data = profesor[0]['sueldo']
        
    if request.method=='POST':
        id = create_form.id.data 
        nombre = create_form.nombre.data
        apellidos = create_form.apellidos.data
        email = create_form.email.data
        especialidad = create_form.especialidad.data
        sueldo = create_form.sueldo.data
        update(id, nombre, apellidos, email, especialidad, sueldo)
    return render_template("update.html", form=create_form, update_profesores=update, ok = ok)

@profesores.route('/delete', methods=['GET', 'POST'])
def delete_teachers():
    create_form = Profesor.ProfesorForm(request.form)
    if request.method == 'GET':
        id = int(request.args.get('id'))
        profesor = search(id)
        create_form.id.data = id
        create_form.nombre.data = profesor[0]['id']
        create_form.nombre.data = profesor[0]['nombre']
        create_form.apellidos.data = profesor[0]['apellidos']
        create_form.email.data = profesor[0]['email']
        create_form.especialidad.data = profesor[0]['especialidad']
        create_form.sueldo.data = profesor[0]['sueldo']
        delete(id)
    return render_template("delete.html", form=create_form, delete_profesores=delete_teachers)


    