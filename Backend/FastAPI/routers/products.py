from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix= "/products", responses={404: {"message": "No Encontrado"}}, tags=["products"])

products_list = ["Producto 1", "Producto 2","Producto 3"]


@router.get("/")
async def products(): return products_list


@router.get("/[id]")
async def products(id:int): return products_list[id]

