# Implementar los métodos de la capa de negocio de socios.

from practico_05.ejercicio_01 import Socio
from practico_05.ejercicio_02 import DatosSocio


class DniRepetido(Exception):
    """Ya existe un socio con ese DNI"""
    pass


class LongitudInvalida(Exception):
    """La longitud del nombre o el apellido es inválida, el nombre y apellido debería ser mayor a 3 caracteres y
    menor a 15 caracteres """
    pass


class MaximoAlcanzado(Exception):
    """Error: La cantidad máxima de socios ya ha sido alcanzada"""
    pass


class NegocioSocio(object):
    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return DatosSocio.buscar(id_socio)

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return DatosSocio.buscar_dni(dni_socio)

    def todos(self):
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        return DatosSocio.todos()

    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        self.regla_1(socio)
        self.regla_2(socio)
        self.regla_3()
        DatosSocio.alta(socio)
        return True

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        return DatosSocio.baja(id_socio)

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        self.regla_2()
        DatosSocio.modificacion(socio)
        return True

    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        try:
            if DatosSocio.buscar_dni(socio.dni):
                raise DniRepetido
            return True
        except DniRepetido:
            print(DniRepetido.__doc__)
            return False

    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        try:
            if 15 < len(socio.nombre) < 3 or 15 < len(socio.apellido) < 3:
                raise LongitudInvalida
            return True
        except LongitudInvalida:
            print(LongitudInvalida.__doc__)
            return False

    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        try:
            if DatosSocio.contar_socios() >= 30:
                raise MaximoAlcanzado
            return True
        except MaximoAlcanzado:
            print(MaximoAlcanzado.__doc__)
            return False
