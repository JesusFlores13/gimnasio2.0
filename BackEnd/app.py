from fastapi import FastAPI
from routes.users import users
from routes.persons import persons
from routes.roles import roles
from routes.usersrols import userrol

app = FastAPI()
app.include_router(users)
app.include_router(persons)
app.include_router(roles)
app.include_router(userrol)
print("Hola bienvenido a mi backend")