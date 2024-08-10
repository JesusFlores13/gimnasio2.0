<<<<<<< HEAD
from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey
from Config.db import Base
import models.users, models.roles
#from sqlalchemy import PrimaryKeyConstraint
#from sqlalchemy.dialects.mysql import LONGTEXT
#from sqlalchemy.orm import relationship

=======
from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

import models.users, models.roles
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b

class UserRol(Base):
    __tablename__ = "tbd_usuarios_roles"

<<<<<<< HEAD
    Usuario_Id = Column(Integer, ForeignKey("tbb_usuarios.Id"),primary_key=True)
    Rol_Id = Column(Integer, ForeignKey("tbc_roles.Id"),primary_key=True)
    Estatus = Column(Boolean, nullable=False, default=True)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)

=======
    Usuario_ID = Column(Integer, ForeignKey("tbb_usuarios.ID"), primary_key=True)
    Rol_ID = Column(Integer, ForeignKey("tbc_roles.ID"), primary_key=True)
    Estatus = Column(Boolean)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b
