"""Base de Datos SQL - Uso de múltiples tablas"""

import datetime as dt
import sqlite3

from practico_04.ejercicio_02 import agregar_persona
from practico_04.ejercicio_04 import buscar_persona
from practico_04.ejercicio_06 import reset_tabla


def agregar_peso(id_persona, fecha, peso):
    """Implementar la funcion agregar_peso, que inserte un registro en la tabla 
    PersonaPeso.

    Debe validar:
    - Que el ID de la persona ingresada existe (reutilizando las funciones ya 
        implementadas).
    - Que no existe de esa persona un registro de fecha posterior al que 
        queremos ingresar.

    Debe devolver:
    - ID del peso registrado.
    - False en caso de no cumplir con alguna validacion."""

    conn = sqlite3.connect('example.db')
    cursor = cursor_peso = conn.cursor()
    sql = """INSERT INTO PERSONAPESO (IDPERSONA, FECHA, PESO)
            VALUES (?,?,?);"""
    sql_consultar_fecha = f"""SELECT FECHA FROM PERSONAPESO WHERE IDPERSONA = {id_persona}"""
    flag = False
    if buscar_persona(id_persona):
        if cursor_peso.execute(sql_consultar_fecha).fetchone():
            fecha_valida = dt.datetime.strptime(cursor_peso.execute(sql_consultar_fecha).fetchone()[0],
                                                '%Y-%m-%d %H:%M:%S')
            if fecha_valida < fecha:
                cursor.execute(sql, (id_persona, fecha, peso))
                flag = True
        else:
            cursor.execute(sql, (id_persona, fecha, peso))
            flag = True
    conn.commit()
    cursor.close()
    cursor_peso.close()
    conn.close()
    return id_persona if flag else False


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', dt.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, dt.datetime(2018, 5, 26), 80) > 0
    # Test Id incorrecto
    assert agregar_peso(200, dt.datetime(1988, 5, 15), 80) is False
    # Test Registro previo al 2018-05-26
    assert agregar_peso(id_juan, dt.datetime(2018, 5, 16), 80) is False


if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
