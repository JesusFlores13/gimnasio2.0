<<<<<<< HEAD
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.dialects.mysql import LONGTEXT
#from sqlalchemy.orm import relationship
from Config.db import Base


class Rol(Base):
    __tablename__ = "tbc_roles"

    Id = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(150))
    Descripcion = Column(Text)
    Estatus = Column(Boolean, nullable=False, default=True)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)

=======
from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class Rol(Base):
    __tablename__ = "tbc_roles"
    
    ID = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255))
    descripcion = Column(String(255))
    estatus = Column(Boolean, default=False)
    created_at = Column(DateTime)
    fecha_actualizacion = Column(DateTime)
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b
