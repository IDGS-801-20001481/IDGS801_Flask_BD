from db import get_conexion

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
    try:
        conn = get_conexion
        with conn.cursor() as cursor:
            cursor.callproc('delete_teacher', args=(id,))
            conn.commit()
        conn.close()
        print('El profesor fue correctamente eliminado')
    except Exception as ex:
        print('Error al intentar eliminar al profesor:', ex)

def get_all():
    try:
        conn = get_conexion()
        with conn.cursor() as cursor:
            cursor.callproc('search_profesor', args="")
            resultset = cursor.fetchall()
            profesores = []
            for row in resultset:
                profesor = {
                    'id': row[0],
                    'nombre': row[1],
                    'apellidos': row[2],
                    'email': row[3],
                    'especialidad': row[4],
                    'sueldo': row[5],
                    'created_date': row[6].strftime('%Y-%m-%d %H:%M:%S')
                }
                profesores.append(profesor)
        conn.close()
        return profesores
    except Exception as ex:
        print('Error al obtener a los profesores:', ex)
        
def search_id(id=None):
    try:
        conn = get_conexion()
        with conn.cursor() as cursor:
            if id:
                cursor.execute('search_profesor_id', args=(id))
            else:
                cursor.execute('search_profesor', args="")
            resultset = cursor.fetchall()
            profesores = []
            for row in resultset:
                profesor = {
                    'id': row[0],
                    'nombre': row[1],
                    'apellidos': row[2],
                    'email': row[3],
                    'especialidad': row[4],
                    'sueldo': row[5],
                    'created_date': row[6].strftime('%Y-%m-%d %H:%M:%S')
                }
                profesores.append(profesor)
        conn.close()
        return profesores
    except Exception as ex:
        print('Error al buscar profesores:', ex)
        
def search(word):
    try:
        conn = get_conexion() 
        with conn.cursor() as cursor:
            cursor.callproc('search_profesor', args=(word,))
            resultset = cursor.fetchall()
            profesores = []
            for row in resultset:
                profesor = {
                    'id': row[0],
                    'nombre': row[1],
                    'apellidos': row[2],
                    'email': row[3],
                    'especialidad': row[4],
                    'sueldo': row[5],
                    'created_date': row[6].strftime('%Y-%m-%d %H:%M:%S')
                }
                profesores.append(profesor)
        conn.close()
        return profesores
    except Exception as ex:
        print('Error al buscar los profesores:', ex)
        return None