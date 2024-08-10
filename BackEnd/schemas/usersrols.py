from typing import List, Union
from pydantic import BaseModel
from datetime import datetime


class UserRolBase(BaseModel):
    Usuario_Id : int
    Rol_Id : int
    estatus:bool 
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime
    #Id_persona:int 
    
class UserRolCreate(UserRolBase):
    pass
class UserRolUpdate(UserRolBase):
    pass

class UserRol(UserRolBase):
    Usuario_Id:int 
    Rol_Id:int 
    #owner_id: int clave foranea
    
    class Config:
        orm_mode = True