from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List

person = APIRouter()
persons: List['model_person' ] = []

# person model
class model_person(BaseModel):
    id:int
    Nombre:str
    primer_apellido: str
    segundo_apellido: str
    titulo_cortecia: str
    fecha_nacimiento: str
    genero: str
    tipo_sangre: str



@person.get("/")
def bienvenida():
    return "Bienvenido al sistema de apis"

@person.get("/person",tags=['Personas'])
def get_usuarios():
    return persons


@person.post("/person",tags=['Personas'])
def save_personas(insert_person: model_person):
    persons.append(insert_person)
    return "Datos guardados"

@person.put("/person/{person_id}",tags=['Personas'])
def update_person(person_id: str, updated_person: model_person):
    for index, person in enumerate(persons):
        if person.id == person_id:
            persons[index] = updated_person
            return {"message": "Usuario actualizado"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@person.delete("/person/{person_id}",tags=['Personas'])
def delete_person(person_id: str):
    for index, person in enumerate(persons):
        if person.id == person_id:
            del persons[index]
            return {"message": "Persona eliminada"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
