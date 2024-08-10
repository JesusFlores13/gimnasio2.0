import models.roles
import schemas.roles
from sqlalchemy.orm import Session
<<<<<<< HEAD
import models, schemas

def get_rol(db: Session, id: int):
    return db.query(models.roles.Rol).filter(models.roles.Rol.id == id).first()

def get_rol_by_nombre(db: Session, rol: str):
    return db.query(models.roles.Rol).filter(models.roles.Rol.Nombre == rol).first()

def get_roles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.roles.Rol).offset(skip).limit(limit).all()

def create_rol(db: Session, rol: schemas.roles.RolCreate):
    db_rol = models.roles.Rol(Nombre=rol.Nombre,
                              Descripcion=rol.Descripcion,
                              Estatus=rol.Estatus,
                              Fecha_Registro=rol.Fecha_Registro,
                              Fecha_Actualizacion=rol.Fecha_Actualizacion)
=======

def get_rol(db:Session, ID:int):
    return db.query(models.roles.Rol).filter(models.roles.Rol.ID == ID).first()

def get_rol_by_nombre(db: Session, nombre: str):
    return db.query(models.roles.Rol).filter(models.roles.Rol == nombre).first()

def get_rols(db: Session, skip:int=0,limit:int=10):
    return db.query(models.roles.Rol).offset(skip).limit(limit).all()

def create_rols(db: Session, roles:schemas.roles.RolCreate):
    db_rol = models.roles.Rol(nombre=roles.nombre,descripcion=roles.descripcion, estatus=roles.estatus,created_at=roles.created_at,fecha_actualizacion=roles.fecha_actualizacion)
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol

<<<<<<< HEAD
def update_rol(db: Session, id: int, rol: schemas.roles.RolUpdate):
    db_rol = db.query(models.roles.Rol).filter(models.roles.Rol.id == id).first()
    if db_rol:
        for var, value in vars(rol).items():
=======
def update_rol(db: Session, ID: int, roles: schemas.roles.RolUpdate):
    db_rol = db.query(models.roles.Rol).filter(models.roles.Rol.ID == ID).first()
    if db_rol:
        for var, value in vars(roles).items():
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b
            setattr(db_rol, var, value) if value else None
        db.commit()
        db.refresh(db_rol)
    return db_rol

<<<<<<< HEAD
def delete_rol(db: Session, id: int):
    db_rol = db.query(models.roles.Rol).filter(models.roles.Rol.id == id).first()
    if db_rol:
        db.delete(db_rol)
        db.commit()
    return db_rol
=======
def delete_rol(db: Session, ID: int):
    db_rol = db.query(models.roles.Rol).filter(models.roles.Rol.ID == ID).first()
    if  db_rol:
        db.delete(db_rol)
        db.commit()
    return db_rol

>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b
