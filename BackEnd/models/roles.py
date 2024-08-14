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

