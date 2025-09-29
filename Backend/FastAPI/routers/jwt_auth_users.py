from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta


ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "de298f6cc05f35655b9b6c3bd186d1a289aab7cec8cb196780cea4b5fa752088" # ---> command to generate it randonmly --openssl rand -hex 32

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str


users_db = {
    "mouredev" : {
        "username": "mouredev",
        "full_name": "Brais Moure",
        "email": "mouredev.com",
        "disabled": False,
        # "password": "123456"
        "password": "$2a$12$jLILhbPKeVsYE0.TWxhmbujkhsTsBfnDHl0rLqLqmpyGRbp1BTzrG"
    },

    "mouredev2" : {
        "username": "mouredev2",
        "full_name": "Brais Moure 2",
        "email": "mouredev.com",
        "disabled": True,
        # "password": "654321"
        "password": "$2a$12$jEDQRyqI0gSBjT6G6NqRU.yMpy0LPJ4.6mhDhxCM1Po/zjWSKmO3."
    },
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)

    if not user_db:
        raise HTTPException( status_code= status.HTTP_400_BAD_REQUEST, detail= "El usuario no es correcto")
    
    user = search_user_db(form.username)

   

    if not  crypt.verify(form.password, user.password):
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail="La contrasena no es correcto")
    
    access_token_expiration = timedelta(minutes=ACCESS_TOKEN_DURATION)

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)

    acces_token = {"sub": user.username,
                    "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}

    return {"access_token" : jwt.encode(acces_token,SECRET, algorithm=ALGORITHM) , "token_type" : "bearer"}


async def auth_user(token: str = Depends(oauth2)):
        exception = HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,
                                detail="Credenciales de autenticacion invalidas",
                                headers={"WWW-Authenticate": "Bearer"})    
        
        try:
            username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")  
            if username is None:  
                raise exception
        except JWTError:
            raise exception
        
        return search_user(username)
            

async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")

    return user

@router.get("/users/me")
async def me(user: User = Depends(current_user)): return user



# to stop mongodb 
# brew services stop mongodb-community@8.2