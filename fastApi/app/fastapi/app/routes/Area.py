from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemas.area import *
from config.db import conn
from funciones.FuncionesNeo4j import *
from neo4j import GraphDatabase
area=APIRouter()



@area.get('/areas')
async def listarArea():
    
    return JSONResponse(status_code=200, content=areasEntidad(conn.SistemaRecomendacion.Area.find()))

