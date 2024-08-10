from fastapi import FastAPI
from routes.user import user
from routes.person import person
from routes.rol import rol
from routes.usersrols import usersrols
from routes.sucursales import sucursales
from routes.equipamiento import equipamiento
from routes.adeudos import adeudo
from routes.mantenimiento import mantenimiento
from routes.instalacion import instalacion 




app=FastAPI()
app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(usersrols)
app.include_router(sucursales)
app.include_router(equipamiento)
app.include_router(adeudo)
app.include_router(mantenimiento)
app.include_router(instalacion)

print("Hola binvenido a mi backend")