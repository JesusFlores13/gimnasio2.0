from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from Config.db import Base

import enum

class MyGenero(enum.Enum):
    M = "M"
    F = "F"
    N_B = "N/B"
    
class MySangre(enum.Enum):
    AP  = "A+ "
    AN = " A-"
    BP = " B+"
    BN = " B-"
    ABP = "AB+"
    ABN = "AB-"
    OP = " O+"
    ON = " O-"
class Person(Base):
    __tablename__ = "tbb_personas"

    Id = Column(Integer, primary_key=True, index=True)
    Titulo_Cortesia = Column(String(80))
    Nombre = Column(String(80))
    Primer_Apellido = Column(String(80))
    Segundo_Apellido = Column(String(80))
    Fecha_Nacimiento = Column(Date)
    Fotografia = Column(LONGTEXT)
    Genero = Column(Enum(MyGenero))
    Tipo_Sangre = Column(Enum(MySangre))
    Estatus = Column(Boolean, default=False)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    #usuarios = relationship("User", back_populates="owner")
    #owner = relationship("tbb_usuarios", back_populates="items")
