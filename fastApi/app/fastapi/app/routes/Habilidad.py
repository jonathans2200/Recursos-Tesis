from fastapi import APIRouter
from fastapi.responses import JSONResponse 

from schemas.area import *
from funciones import FuncionesNeo4j,FuncionesMongo
import pandas as pd
from config.db import conn
import json


from schemas.habilidad import habilidadEntidad, habilidadesEntidad

habilidad=APIRouter()


@habilidad.get('/habilidad')
async def obtenerHabilidadCompetencia(codigo:str):
  
    resultado = []
    resu_query =FuncionesNeo4j.listarHabilidadCompetencia(codCompetencia=codigo)
    if resu_query.empty == True:
        return  JSONResponse(status_code=404, content={"message": "Item no encontrado"})
    else:
 
        mongo = pd.DataFrame(FuncionesMongo.listarHabilidadCompetencia(codCompetencia=codigo))
        for i in resu_query.iloc[:,0]:
            comparar = mongo.loc[mongo['codigo'] == i]
            if (len(comparar) > 0):
                comparar = comparar.to_dict('records')
                for s in comparar:      
                    resultado.append(s)
        fina=json.dumps(resultado)

    return JSONResponse(status_code=200, content=json.loads(fina))
  




@habilidad.get('/buscarHabilidad')
async def buscarHabilidad(palabra:str):
    return habilidadesEntidad(conn.SistemaRecomendacion.Habilidad.find({"nombre":{"$regex": palabra, "$options": "i"}}).limit(15))



@habilidad.get('/detalleHabilidad')
async def detalleHabilidad(codigo:str):
    resultado=conn.SistemaRecomendacion.Habilidad.find_one({'codigo':codigo},{'_id':False})
  
    return resultado
