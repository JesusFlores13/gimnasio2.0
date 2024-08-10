from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.roles, Config.db, schemas.roles, models.roles
from typing import List

key=Fernet.generate_key()
f = Fernet(key)

rol = APIRouter()

models.roles.Base.metadata.create_all(bind=Config.db.engine)

def get_db():
    db = Config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@rol.get("/roles/", response_model=List[schemas.roles.Rol], tags=["Roles"])
def read_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_roles= crud.roles.get_roles(db=db, skip=skip, limit=limit)
    return db_roles

@rol.post("/rol/{id}", response_model=schemas.roles.Rol, tags=["Roles"])
def read_rol(id: int, db: Session = Depends(get_db)):
    db_rol= crud.roles.get_rol(db=db, id=id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return db_rol

@rol.post("/rol/", response_model=schemas.roles.Rol, tags=["Roles"])
def create_rol(rol: schemas.roles.RolCreate, db: Session = Depends(get_db)):
    db_rol = crud.roles.get_rol_by_nombre(db, rol=rol.Nombre)
    if db_rol:
        raise HTTPException(status_code=400, detail="Usuario existente intenta nuevamente")
    return crud.roles.create_rol(db=db, rol=rol)

@rol.put("/rol/{id}", response_model=schemas.roles.Rol, tags=["Roles"])
def update_rol(id: int, rol: schemas.roles.RolUpdate, db: Session = Depends(get_db)):
    db_rol = crud.roles.update_rol(db=db, id=id, rol=rol)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no actualizado")
    return db_rol

@rol.delete("/rol/{id}", response_model=schemas.roles.Rol, tags=["Roles"])
def delete_rol(id: int, db: Session = Depends(get_db)):
    db_rol = crud.roles.delete_rol(db=db, id=id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no se pudo eliminar")
    return db_rol