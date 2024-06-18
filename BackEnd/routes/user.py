from fastapi import APIRouter

user = APIRouter()

@user.get("/users")

def helloword():
    return "Hola 9B"