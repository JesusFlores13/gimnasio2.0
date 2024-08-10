<<<<<<< HEAD
from typing import List, Union, Optional
from pydantic  import BaseModel
=======
from typing import List, Optional, Union
from pydantic import BaseModel
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b
from datetime import datetime

from models.users import MyEstatus

class UserBase(BaseModel):
<<<<<<< HEAD
    Persona_Id: int
    Nombre_Usuario:str
    Contrasena:str
    Correo_Electronico:str
    Numero_Telefononico_Movil:str
    Estatus:str
=======
    Persona_ID: int
    Nombre_Usuario: str
    Correo_Electronico: str
    Contrasena: str
    Numero_Telefonico_Movil: str
    Estatus: MyEstatus
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
<<<<<<< HEAD
    Id:int
    Persona_Id:int
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    Nombre_Usuario: Optional[str] = None
    Correo_Electronico: Optional[str]= None
    Contrasena: str
    Numero_Telefonico_Movil: Optional[str]=None


=======
    ID: int
    Persona_ID: int
    class Config:
        orm_mode = True
        
class UserLogin(BaseModel):
    Nombre_Usuario: Optional[str]=None
    Correo_Electronico:Optional[str]=None
    Contrasena: str
    Numero_Telefonico_Movil: Optional[str]=None
   
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b
