from fastapi import APIRouter,HTTPException
from fastapi.responses import JSONResponse
from config.db import conn
from schemas.area import *
from schemas.encuesta import encuestaEntidad
from funciones import FuncionesNeo4j,FuncionesMongo
import pandas as pd
import json

encuesta=APIRouter()


@encuesta.get('/crearEncuesta')
async  def crearEncuesta(pregunta1:float,pregunta2:float,pregunta3:float,pregunta4:float,codigo_usuario:str,codigo_habilidad:str):
    nuevaEncuesta={"pregunta1":pregunta1,"pregunta2":pregunta2,"pregunta3":pregunta3,"pregunta4":pregunta4,"codigo_usuario":codigo_usuario,"codigo_habilidad":codigo_habilidad}
    id = conn.SistemaRecomendacion.Encuesta.insert_one(nuevaEncuesta).inserted_id
    usuario=conn.SistemaRecomendacion.Encuesta.find_one({'_id':id})
    return encuestaEntidad(usuario)
    



@encuesta.get('/verficarEncuesta')
async  def crearEncuesta(codigo_usuario:str,codigo_habilidad:str):
    u=conn.SistemaRecomendacion.Encuesta.find_one({'codigo_usuario':codigo_usuario,'codigo_habilidad':codigo_habilidad})
  
    if u is not None:
        return JSONResponse(status_code=200, content={"estado": "True"})
    else :
         return JSONResponse(status_code=200, content={"estado": "False"})





@encuesta.get('/graficaHabilidades')
async  def grafica():
    u= conn.SistemaRecomendacion.Encuesta.aggregate(
        [
       {"$group":
        {"_id":"$codigo_habilidad","total_pregunta":{"$sum":1},
            "pregunta1_promedio":{"$avg":"$pregunta1"},
            "pregunta2_promedio":{"$avg":"$pregunta2"},
            "pregunta3_promedio":{"$avg":"$pregunta3"},
            "pregunta4_promedio":{"$avg":"$pregunta4"}
        
        }
       },
       {'$addFields':
            {
            "pregunta1_promedio":{"$round":['$pregunta1_promedio',1] },
            "pregunta2_promedio":{"$round":['$pregunta2_promedio',1] },
            "pregunta3_promedio":{"$round":['$pregunta3_promedio',1] },
            "pregunta4_promedio":{"$round":['$pregunta4_promedio',1] },
            }
        
        }
       ])
    datos=pd.DataFrame(list(u))
    dato=datos.to_json(orient='records')

    return JSONResponse(status_code=200, content=json.loads(dato))





@encuesta.get('/graficaHabilidad')
async  def graficaHabilidad(codigo:str):
    u= conn.SistemaRecomendacion.Encuesta.aggregate(
[
    {
        "$match":{"codigo_habilidad":codigo}
    },
    {"$group":
        {"_id":"$codigo_habilidad","total_pregunta":{"$sum":1},
            "pregunta1_promedio":{"$avg":"$pregunta1"},
            "pregunta2_promedio":{"$avg":"$pregunta2"},
            "pregunta3_promedio":{"$avg":"$pregunta3"},
            "pregunta4_promedio":{"$avg":"$pregunta4"}
        
        }
    },
    {'$addFields':
            {
            "pregunta1_promedio":{"$round":['$pregunta1_promedio',1] },
            "pregunta2_promedio":{"$round":['$pregunta2_promedio',1] },
            "pregunta3_promedio":{"$round":['$pregunta3_promedio',1] },
            "pregunta4_promedio":{"$round":['$pregunta4_promedio',1] },
            }
        
        }
]

    )

    datos=pd.DataFrame(list(u))
    dato=datos.to_json(orient='records')

    return JSONResponse(status_code=200, content=json.loads(dato))