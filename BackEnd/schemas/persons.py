<<<<<<< HEAD
from typing import List, Union
from pydantic  import BaseModel
from datetime import datetime, date
from sqlalchemy.dialects.mysql import BIT
=======
from typing import List,Union
from pydantic import BaseModel
from datetime import datetime
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b

from models.persons import MyGenero, MySangre

class PersonBase(BaseModel):
<<<<<<< HEAD
    Titulo_Cortesia : str
    Nombre : str
    Primer_Apellido : str
    Segundo_Apellido : str
    Fecha_Nacimiento : date
    Fotografia : str
    Genero : str
    Tipo_Sangre : str
    Estatus:bool
    Fecha_Registro : datetime
    Fecha_Actualizacion : datetime
    
=======
    
    Titulo_Cortesia:str
    Nombre: str
    Primer_Apellido: str
    Segundo_Apellido: str
    Genero: MyGenero
    Tipo_Sangre:  MySangre  
    Fecha_Nacimiento: datetime
    Fotografia:str
    Telefono: str
    Correo_Electronico: str
    Estatus:bool
    Fecha_Registro:datetime
    Fecha_Actualizacion:datetime
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b


    
    
class PersonCreate(PersonBase):
    pass
class PersonUpdate(PersonBase):
    pass
class Person(PersonBase):
<<<<<<< HEAD
    Id:int
    
    class Config:
        orm_mode = True

=======
    ID: int

    class Config:
        orm_mode = True
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b
