from db import get_conexion
import json

def insert(nombre, apellidos, email, especialidad, sueldo):
    ok = ''
    try:
        conn = get_conexion()
        with conn.cursor() as cursor:
            cursor.callproc('insertar_profesor', args=(nombre, apellidos, email, especialidad, sueldo))
            conn.commit()
        conn.close()
        print("Profesor Añadido correctamente a la base de datos")
        ok= "Profesor agregado correctamente"
    except Exception as ex:
        print("Error al agregar al profesor")
        ok = "Error al agregar al profesor", ex
    return ok
    
    
def update(id,nombre, apellidos, email, especialidad, sueldo):
    ok = ''
    try:
        conn = get_conexion()
        with conn.cursor() as cursor:
            cursor.callproc('actualizar_profesor', args=(id,nombre, apellidos, email, especialidad, sueldo))
            conn.commit()
        conn.close()
        print("Profesor Añadido correctamente a la base de datos")
    except Exception as ex:
        print("Error al agregar al profesor")
        
def delete(id):
    print(id)
    try:
        conn = get_conexion()
        with conn.cursor() as cursor:
            cursor.execute('call eliminar_profesor('+ str(id) +')')
            conn.commit()
        conn.close()
        print('El profesor fue correctamente eliminado')
    except Exception as ex:
        print('Error al intentar eliminar al profesor:', ex)

def get_all():
    try:
        conn = get_conexion()
        with conn.cursor() as cursor:
            cursor.callproc('get_all_profesor')
            resultset = cursor.fetchall()

        conn.close()
        return resultset
    except Exception as ex:
        print('Error al obtener a los profesores:', ex)
        
def search(word):
    try:
        conn = get_conexion()
        with conn.cursor() as cursor:
            if int(word) / 1 == int(word):
                cursor.execute('call search_profesor_id('+ str(word) +')')
            else:
                print('Entro Aqui')
                cursor.callproc('call search_profesor('+ str(word) +')')
            resultset = cursor.fetchall()
            print(resultset)
        conn.close()
        return resultset
    except Exception as ex:
        print('Error al buscar profesores:', ex)
        
        