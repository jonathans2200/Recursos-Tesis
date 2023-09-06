from fastapi import APIRouter
from config.db import conn
from schemas.video import *
from schemas.programa import *
from funciones.webCrawler import *
from funciones import FuncionesNeo4j,FuncionesMongo
import pandas as pd
from fastapi.responses import JSONResponse
import json

links=APIRouter()


@links.get('/links')
async def videos(identificador:str):
    datos=videosEntidad(conn.SistemaRecomendacion.Video.find({"identificador": identificador}))
    if(datos):
        return datos
    else:
        return JSONResponse(status_code=404, content={"message": "false"})

@links.get('/linkPrograma')
async def videos(identificador:str):
    return programasEntidad(conn.SistemaRecomendacion.Programas.find({"identificador": identificador}))







@links.get('/programaData')
async def getProgramaData(codigo:str):
    resu_query =webProgramaLink(codigo=codigo)
    dato = resu_query.to_json(orient='records')
   

    return JSONResponse(status_code=200, content=json.loads(dato))