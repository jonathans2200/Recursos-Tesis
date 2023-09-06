from fastapi import APIRouter
from schemas.area import *
from funciones import FuncionesNeo4j,FuncionesMongo
import pandas as pd
from fastapi.responses import JSONResponse
import json

competencia=APIRouter()


@competencia.get('/competencia')
async  def obtenerCompetenciaBloque(codigo:str):

    resultado = []
    resu_query =FuncionesNeo4j.listarCompetenciaBloque(codBloque=codigo)
    if resu_query.empty == True:
        return  JSONResponse(status_code=404, content={"message": "Item no encontrado"})
    else:
        mongo = pd.DataFrame(FuncionesMongo.listarCompetenciaBloque(codBloque=codigo))
        for i in resu_query.iloc[:,0]:
            comparar = mongo.loc[mongo['codigo'] == i]
            if (len(comparar) > 0):
                comparar = comparar.to_dict('records')
                for s in comparar:      
                   resultado.append(s)
        fina=json.dumps(resultado)

    return JSONResponse(status_code=200, content=json.loads(fina))

