from typing import List, Union
from pydantic  import BaseModel
from datetime import datetime, date
from sqlalchemy.dialects.mysql import BIT
from fastapi.middleware.cors import CORSMiddleware
from models.persons import MyGenero, MySangre

class PersonBase(BaseModel):
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
    


    
    
class PersonCreate(PersonBase):
    pass
class PersonUpdate(PersonBase):
    pass
class Person(PersonBase):
    Id:int
    
    class Config:
        orm_mode = True

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Cambia esto a la URL de tu frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los encabezados
)