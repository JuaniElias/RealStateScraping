"""Base de Datos SQL - Alta"""

import datetime
import sqlite3

from ejercicio_01 import reset_tabla


def agregar_persona(nombre, nacimiento, dni, altura):
    """Implementar la función agregar_persona, que inserte un registro en la
    tabla Persona y devuelva los datos ingresados el id del nuevo registro."""
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    sql_insert = """insert into persona (nombre, fechanacimiento, dni, altura)
    values (?, ?, ?, ?);"""
    cursor.execute(sql_insert, (nombre, nacimiento, dni, altura))
    sql_request_id = """select max(idpersona) from persona"""
    cursor.execute(sql_request_id)
    id_persona = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return id_persona


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan


if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
