"""Base de Datos - Creación de Clase en ORM"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Socio(Base):
    """Implementar un modelo Socio a través de Alchemy que cuente con los siguientes campos:
        - id_socio: entero (clave primaria, auto-incremental, único)
        - dni: entero (único)
        - nombre: string (longitud 250)
        - apellido: string (longitud 250)
    """
    __tablename__ = 'socios'
    id = Column("id_socio", Integer, primary_key=True, nullable=False)
    dni = Column(Integer, unique=True, nullable=False)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
