from jwt import encode, decode

<<<<<<< HEAD
def solicita_token (dato:dict)->str:
    token:str=encode(payload=dato,key='mi_clave',algorithm='HS256')
    return token
def valida_token(token:str)->dict:
    dato:dict = decode(token, key='mi_clave',algorithms=['HS256'])
    return dato 
=======
def solicita_token (dato:dict) ->str:
    token:str=encode(payload=dato,key='mi_clave', algorithm='HS256')
    return token

def valida_token(token:str)->dict:
    dato:dict = decode(token,key='mi_clave', algorithms=['HS256'])
    return dato
>>>>>>> fb76b8eb2713d5e06970296b92d97f81e6b2546b
