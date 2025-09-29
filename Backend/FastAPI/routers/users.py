from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter()

# Inicia el server: uvicorn users:app --reload

# Entidad user

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str

users_list = [
        User(id = 1,name= "Brais", surname = "More",url = "https://"),
        User(id = 2,name = "Daniel",surname = "Caballero",url = "https://"),
        User(id = 3,name = "Manuel",surname = "Caballero",url = "https://"),
        ]

@router.get("/usersjson")
async def usersjson(): return [{"name": "Daniel", "surname":"Caballero","url":"https://"},
                          {"name": "Manuel", "surname":"Caballero","url":"https://"},
                          {"name": "Karol", "surname":"Caballero","url":"https://"}
                          ]


@router.get("/users")
async def users(): return users_list


# Path parametros que son necesarios para la peticion
@router.get("/user/{id}")
async def user(id: int): 
    return search_user(id = id)
    
# Query son parametros que no son tan necesarios para hacer la peticion
@router.get("/userquery/")
async def user(id: int): 
    return search_user(id = id)
    
def search_user(id: int): 
    users = filter(lambda user:user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ah encontrado el usuario"}

@router.post("/user/",response_model = user, status_code=201)
async def user(user:User):
    if type(search_user(user.id)) == User:
       raise HTTPException(status_code = 204, detail = "El usuario ya existe")
    else:
        users_list.append(user)

    return user


@router.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found: return{"error": "No se ha encontrado el usuario"}
    else: return user


@router.delete("/user/{id}")
async def user(id:int):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found: return {"error": "No se a eliminado el usuario"}