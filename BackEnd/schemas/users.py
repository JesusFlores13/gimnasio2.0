from typing import List, Union, Optional
from pydantic  import BaseModel
from datetime import datetime

from models.users import MyEstatus

class UserBase(BaseModel):
    Persona_Id: int
    Nombre_Usuario:str
    Contrasena:str
    Correo_Electronico:str
    Numero_Telefonico_Movil:str
    Estatus:str
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    Id:int
    #Persona_Id:int
    class Config:
        orm_mode = True

       
class UserLogin(BaseModel):
    Nombre_Usuario: Optional[str] = None
    Correo_Electronico: Optional[str]= None
    Contrasena: str
    Numero_Telefonico_Movil: Optional[str]=None


