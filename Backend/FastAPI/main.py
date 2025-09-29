from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)


app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)

app.include_router(users_db.router)

app.mount("/static", StaticFiles(directory = "static"), name="Static") # Para montar recursos staticos. Ex: Imagenes


@app.get("/")
async def root(): return "Hola Mundo"

@app.get("/url")
async def root(): return {"url_curso":"https://danielCaballero.com"}

# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentacion Swagger: http://127.0.0.1:8000/docs
# Documentacion Redocly: http://127.0.0.1:8000/redoc