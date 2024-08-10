import models.users
import schemas.users
from sqlalchemy.orm import Session
import models, schemas

<<<<<<< HEAD
# Busqueda por id
def get_user(db:Session, id: int):
    return db.query(models.users.User).filter(models.users.User.Id == id).first()

# Busqueda por USUARIO
def get_user_by_usuario(db:Session, usuario: str):
    return db.query(models.users.User).filter(models.users.User.Nombre_Usuario == usuario).first()
=======
def get_user(db: Session, id: int):
    return db.query(models.users.User).filter(models.users.User.ID == id).first()

def get_user_by_usuario(db: Session, usuario: str):
    return db.query(models.users.User).filter(models.users.User.Nombre_Usuario == usuario).first()

def get_user_by_credentials(db: Session, usuario: str,Correo_Electronico:str,Telefono:str, password:str):
    return db.query(models.users.User).filter((models.users.User.Nombre_Usuario == usuario) | 
                                              (models.users.User.Correo_Electronico==Correo_Electronico)|
                                              (models.users.User.Numero_Telefonico_Movil==Telefono),
                                              models.users.User.Contrasena == password).first()
    
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b

# 
def get_user_by_creentials(db: Session, username: str,  correo: str, telefono: str,password: str):
    return db.query(models.users.User).filter((models.users.User.Nombre_Usuario == username) |
                                               (models.users.User.Correo_Electronico == correo) | 
                                               (models.users.User.Numero_Telefononico_Movil == telefono),
                                                 models.users.User.Contrasena == password).first()

# Buscar todos los usuarios
def get_users(db:Session, skip: int=0, limit:int=10):
    return db.query(models.users.User).offset(skip).limit(limit).all()

<<<<<<< HEAD
# Crear nuevo usuario
def create_user(db:Session, user: schemas.users.UserCreate):
    db_user = models.users.User(Persona_Id=user.Persona_Id,
                                Nombre_Usuario=user.Nombre_Usuario, 
                                Correo_Electronico=user.Correo_Electronico,
                                Contrasena=user.Contrasena, 
                                Numero_Telefononico_Movil=user.Numero_Telefononico_Movil, 
                                Estatus=user.Estatus, 
                                Fecha_Registro=user.Fecha_Registro, 
                                Fecha_Actualizacion=user.Fecha_Actualizacion)
=======
def create_user(db: Session, user: schemas.users.UserCreate):
    db_user = models.users.User(Persona_ID = user.Persona_ID, Nombre_Usuario=user.Nombre_Usuario,Correo_Electronico = user.Correo_Electronico,Contrasena = user.Contrasena, Numero_Telefonico_Movil=user.Numero_Telefonico_Movil, Estatus=user.Estatus,Fecha_Registro = user.Fecha_Registro,Fecha_Actualizacion = user.Fecha_Actualizacion 
)
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    print(db_user)
    return db_user

<<<<<<< HEAD
# Actualizar un usuario por id
def update_user(db:Session, id:int, user:schemas.users.UserUpdate):
    db_user = db.query(models.users.User).filter(models.users.User.Id == id).first()
=======
def update_user(db: Session, id: int, user: schemas.users.UserUpdate):
    db_user = db.query(models.users.User).filter(models.users.User.ID == id).first()
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b
    if db_user:
        for var, value in vars(user).items():
            setattr(db_user, var, value) if value else None
        db.commit()
        db.refresh(db_user)
    return db_user

<<<<<<< HEAD
# Eliminar un usuario por id
def delete_user(db:Session, id:int):
    db_user = db.query(models.users.User).filter(models.users.User.Id == id).first()
=======
def delete_user(db: Session, id: int):
    db_user = db.query(models.users.User).filter(models.users.User.ID == id).first()
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user