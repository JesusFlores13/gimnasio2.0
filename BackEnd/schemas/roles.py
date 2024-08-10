from typing import List, Union
from pydantic import BaseModel
from datetime import datetime


class RolBase(BaseModel):
    Nombre : str
    Descripcion: str
    estatus:bool 
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime
    #Id_persona:int 
    
class RolCreate(RolBase):
    pass
class RolUpdate(RolBase):
    pass

class Rol(RolBase):
    id:int 
    #owner_id: int clave foranea
    
    class Config:
        orm_mode = True