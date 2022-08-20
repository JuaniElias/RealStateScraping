# Implementar los metodos de la capa de negocio de socios.

from practico_05.ejercicio_01 import Socio
from practico_05.ejercicio_02 import DatosSocio

class DniRepetido(Exception):
    def __init__(self):
        super(DniRepetido, self).__init__('DNI Repetido')


class LongitudInvalida(Exception):
    def __init__(self, msg):
        super(LongitudInvalida, self).__init__(msg)


class MaximoAlcanzado(Exception):
    def __init__(self):
        super(MaximoAlcanzado, self).__init__('Se alcanzó el máximo de socios')


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
        return self.datos.buscar(id_socio)

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return self.datos.buscar_dni(dni_socio)

    def todos(self):
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        return self.datos.todos()

    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        try:
            if self.regla_1(socio) and self.regla_2(socio) and self.regla_3():
                self.datos.alta(socio)
                return True
        except Exception as ex:
            raise ex

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        return self.datos.baja(id_socio)

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        try:
            if self.regla_1(socio):
                self.datos.modificacion(socio)
            return True
        except Exception as ex:
            raise ex

    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        enc = self.buscar_dni(socio.dni)
        if enc is None:
            return True
        raise DniRepetido()

    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        if self.MIN_CARACTERES < len(socio.nombre) < self.MAX_CARACTERES:
            if self.MIN_CARACTERES < len(socio.apellido) < self.MAX_CARACTERES:
                return True
            else:
                raise LongitudInvalida("Longitud del apellido invalida")
        else:
            raise LongitudInvalida("Longitud del nombre invalida")

    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        if len(self.datos.todos()) < self.MAX_SOCIOS:
            return True
        raise MaximoAlcanzado()