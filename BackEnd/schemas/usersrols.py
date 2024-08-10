<<<<<<< HEAD
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
=======
from typing import List,Union
from pydantic import BaseModel
from datetime import datetime

class UserRolBase(BaseModel):
    Usuario_ID: int
    Rol_ID: int
    Estatus: bool
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class UserRolCreate(UserRolBase):
    pass

>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b
class UserRolUpdate(UserRolBase):
    pass

class UserRol(UserRolBase):
<<<<<<< HEAD
    Usuario_Id:int 
    Rol_Id:int 
    #owner_id: int clave foranea
=======
    Usuario_ID: int
    Rol_ID: int
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b
    
    class Config:
        orm_mode = True