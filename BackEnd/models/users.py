<<<<<<< HEAD
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from Config.db import Base
=======
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b
import models.persons
import enum

class MyEstatus(enum.Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"
    Bloqueado = "Bloqueado"
    Suspendido = "Suspendido"
<<<<<<< HEAD

class User(Base):
    __tablename__ = 'tbb_usuarios'
    Id = Column(Integer, primary_key=True, index=True)
    Persona_Id = Column(Integer, ForeignKey("tbb_personas.Id"))
    Nombre_Usuario = Column(String(60))
    Correo_Electronico = Column(String(100))
    Contrasena = Column(String(40))
    Numero_Telefononico_Movil = Column(String(20))
    Estatus = Column( Enum(MyEstatus))
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
=======
    

class User(Base):
    __tablename__ = "tbb_usuarios"

    ID = Column(Integer, primary_key=True, index=True)
    Persona_ID = Column(Integer, ForeignKey("tbb_personas.ID"))
    Nombre_Usuario = Column(String(60))
    Correo_Electronico = Column(String(100))
    Contrasena = Column(String(40))
    Numero_Telefonico_Movil = Column(String(20))
    Estatus = Column(Enum(MyEstatus))
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b
