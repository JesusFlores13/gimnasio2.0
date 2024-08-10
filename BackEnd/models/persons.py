<<<<<<< HEAD
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from Config.db import Base
=======
from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey,Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class MyGenero(enum.Enum):
    Masculino ="Masculino"
    Femenino ="Femenino"
    Otro = "Otro"
class MySangre(enum.Enum):
    AP="A+"
    AN="A-"
    BP="B+"
    BN="B-"
    ABP="AB+"
    ABN="AB-"
    OP="O+"
    ON="O-"
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b

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
<<<<<<< HEAD

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
=======
    
    ID = Column(Integer, primary_key=True, index=True)
    Titulo_Cortesia = Column(String(255))
    Nombre = Column(String(255))
    Primer_Apellido = Column(String(255))
    Segundo_Apellido = Column(String(255))
    Genero = Column(Enum(MyGenero))  
    Tipo_Sangre = Column(Enum(MySangre)) 
    Fecha_Nacimiento = Column(DateTime)
    Fotografia = Column(String(255))
    Telefono = Column(String(20)) 
    Correo_Electronico = Column(String(255))
    Estatus = Column(Boolean, default=False)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b
