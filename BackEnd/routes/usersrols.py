<<<<<<< HEAD
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.usersrols, Config.db, schemas.usersrols, models.usersrols
from typing import List

key=Fernet.generate_key()
f = Fernet(key)

usersrols = APIRouter()

models.usersrols.Base.metadata.create_all(bind=Config.db.engine)

def get_db():
    db = Config.db.SessionLocal()
=======
from fastapi import APIRouter,HTTPException,Depends,Request
from sqlalchemy.orm import Session
from portadortoken import Portador
import crud.usersrols, config.db, schemas.usersrols, models.usersrols
from typing import List

userrol = APIRouter()

models.usersrols.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b
    try:
        yield db
    finally:
        db.close()
<<<<<<< HEAD

@usersrols.get("/roles/", response_model=List[schemas.roles.Rol], tags=["User Roles"])
def read_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_roles= crud.roles.get_roles(db=db, skip=skip, limit=limit)
    return db_roles

@usersrols.post("/rol/{id}", response_model=schemas.roles.Rol, tags=["User Roles"])
def read_rol(id: int, db: Session = Depends(get_db)):
    db_rol= crud.roles.get_rol(db=db, id=id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return db_rol

@usersrols.post("/rol/", response_model=schemas.roles.Rol, tags=["User Roles"])
def create_rol(rol: schemas.roles.RolCreate, db: Session = Depends(get_db)):
    db_rol = crud.roles.get_rol_by_nombre(db, rol=rol.Nombre)
    if db_rol:
        raise HTTPException(status_code=400, detail="Usuario existente intenta nuevamente")
    return crud.roles.create_rol(db=db, rol=rol)

@usersrols.put("/rol/{id}", response_model=schemas.roles.Rol, tags=["User Roles"])
def update_rol(id: int, rol: schemas.roles.RolUpdate, db: Session = Depends(get_db)):
    db_rol = crud.roles.update_rol(db=db, id=id, rol=rol)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no actualizado")
    return db_rol

@usersrols.delete("/rol/{id}", response_model=schemas.roles.Rol, tags=["User Roles"])
def delete_rol(id: int, db: Session = Depends(get_db)):
    db_rol = crud.roles.delete_rol(db=db, id=id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no se pudo eliminar")
    return db_rol
=======
        
@userrol.get("/usersrols/", response_model=List[schemas.usersrols.UserRol], tags=["Usuarios Roles"] ,dependencies=[Depends(Portador())])
def read_usersrols(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_usersrols= crud.usersrols.get_usersrols(db=db, skip=skip, limit=limit)
    return db_usersrols

@userrol.post("/userrol/{id_user}/{id_rol}", response_model=schemas.usersrols.UserRol, tags=["Usuarios Roles"] ,dependencies=[Depends(Portador())])
def read_UserRol(id_user: int, id_rol: int, db: Session = Depends(get_db)):
    db_userrol= crud.usersrols.get_userrol(db=db, id_user=id_user,id_rol=id_rol)

    if db_userrol is None:
        raise HTTPException(status_code=404, detail="UserRol no existe")
    return db_userrol
    order = db.query(Order).filter(Order.order_id == order_id, Order.product_id == product_id).first()


@userrol.post("/userrols/", response_model=schemas.usersrols.UserRol, tags=["Usuarios Roles"])
def create_userRol(userrol: schemas.usersrols.UserRolCreate, db: Session = Depends(get_db)):
    db_userrol = crud.usersrols.get_userrol(db=db, id_user=userrol.Usuario_ID, id_rol=userrol.Rol_ID)
    print (db_userrol)
    if db_userrol:
        raise HTTPException(status_code=400, detail="Usuario existente intenta nuevamente")
    return crud.usersrols.create_userrol(db=db, userrol=userrol)

@userrol.put("/userrol/{id_user}/{id_rol}", response_model=schemas.usersrols.UserRol, tags=["Usuarios Roles"] ,dependencies=[Depends(Portador())])
def update_user(id_user: int, id_rol: int, userrol: schemas.usersrols.UserRolUpdate, db: Session = Depends(get_db)):
    db_userrol = crud.usersrols.update_userrol(db=db, id_user=id_user, id_rol=id_rol, userrol=userrol)
    print (db_userrol.Estatus)
    if db_userrol is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no actualizado")
    return db_userrol

@userrol.delete("/userrol/{id_user}/{id_rol}", response_model=schemas.usersrols.UserRol, tags=["Usuarios Roles"] ,dependencies=[Depends(Portador())])
def delete_rol(id_user: int, id_rol: int, db: Session = Depends(get_db)):
    db_userrol = crud.usersrols.delete_userrol(db=db, id_user=id_user, id_rol=id_rol)
    if db_userrol is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no se pudo eliminar")
    return db_userrol
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b
