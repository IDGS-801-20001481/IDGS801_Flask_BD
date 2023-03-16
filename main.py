from db import get_connection

'''try:
        connection = get_connection()
        with connection.cursor() as curso:
            curso.execute('call consulta_alumnos()')
            resultset = curso.fetchball()
            for row in resultset:
                print(row)
            connection.close()
    except Exception as ex:
        print('Error')'''
        
try:
    connection = get_connection()
    with connection.cursor() as curso:
        curso.execute('call consulta_alumnos(%s)',(2,))
        resultset = curso.fetchball()
        for row in resultset:
            print(row)
        connection.close()
except Exception as ex:
    print('Error')