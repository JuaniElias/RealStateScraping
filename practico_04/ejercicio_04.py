"""Base de Datos SQL - Búsqueda"""

import datetime
import sqlite3

from practico_04.ejercicio_01 import reset_tabla
from practico_04.ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    """Implementar la funcion buscar_persona, que devuelve el registro de una
    persona basado en su id. El return es una tupla que contiene sus campos:
    id, nombre, nacimiento, dni y altura. Si no encuentra ningun registro,
    devuelve False."""
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    sql_select = f"select * from persona where persona.idpersona = {id_persona};"
    cursor.execute(sql_select)
    pers_selecc = cursor.fetchone()
    if pers_selecc is None:
        return False
    id, nombre, nacimiento, dni, altura = pers_selecc[0], pers_selecc[1], datetime.datetime.strptime(pers_selecc[2], '%Y-%m-%d %H:%M:%S'), pers_selecc[3], pers_selecc[4]
    cursor.close()
    conn.close()
    pers_selecc = (id, nombre, nacimiento, dni, altura)
    return pers_selecc


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False


if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
