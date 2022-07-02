"""Base de Datos SQL - Baja"""

import datetime
import sqlite3

from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    """Implementar la función borrar_persona, que elimina un registro en la
    tabla Persona. Devuelve un booleano en base a si encontró el registro y lo
    borro o no."""
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    sql_delete = f"delete from persona where persona.idpersona = {id_persona};"
    cursor.execute(sql_delete)
    filas_modificadas = cursor.rowcount
    conn.commit()
    conn.close()
    return True if filas_modificadas > 0 else False


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False


if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
