from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey
from Config.db import Base
import models.users, models.roles
#from sqlalchemy import PrimaryKeyConstraint
#from sqlalchemy.dialects.mysql import LONGTEXT
#from sqlalchemy.orm import relationship


class UserRol(Base):
    __tablename__ = "tbd_usuarios_roles"

    Usuario_Id = Column(Integer, ForeignKey("tbb_usuarios.Id"),primary_key=True)
    Rol_Id = Column(Integer, ForeignKey("tbc_roles.Id"),primary_key=True)
    Estatus = Column(Boolean, nullable=False, default=True)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)

