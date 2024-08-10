<<<<<<< HEAD
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
=======
from typing import List,Union
from pydantic import BaseModel
from datetime import datetime

class RolBase(BaseModel):
    nombre: str
    descripcion: str
    estatus:bool
    created_at:datetime
    fecha_actualizacion:datetime

    
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b
    
class RolCreate(RolBase):
    pass
class RolUpdate(RolBase):
    pass
<<<<<<< HEAD

class Rol(RolBase):
    id:int 
    #owner_id: int clave foranea
    
    class Config:
        orm_mode = True
=======
class Rol(RolBase):
    ID:int
    #owner_id:int clave foranea
    
    class Config:
        orm_mode=True
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b
