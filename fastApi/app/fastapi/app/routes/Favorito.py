from fastapi import APIRouter,HTTPException
from fastapi.responses import JSONResponse
from config.db import conn
from schemas.area import *
from schemas.habilidad import *

from funciones import FuncionesNeo4j,FuncionesMongo
import pandas as pd
import json

favorito=APIRouter()


@favorito.get('/addFavorito')
async def crearFavorito(usuario:str,habilidad:str,puntaje:float):

    u=conn.SistemaRecomendacion.Usuario.find_one({'codigo':usuario})
    h=conn.SistemaRecomendacion.Habilidad.find_one({'codigo':habilidad})
    if u is not None and h is not  None :
        resu_query =FuncionesNeo4j.CrearFavorito(usuario=u['codigo'],habilidad=h['codigo'],puntaje=puntaje)
        return JSONResponse(status_code=200, content=resu_query)
    else:
        return JSONResponse(status_code=204, content=resu_query)

@favorito.get('/estadoFavorito')
async def verificarFavorito(usuario:str,habilidad:str):

    u=conn.SistemaRecomendacion.Usuario.find_one({'codigo':usuario})
    h=conn.SistemaRecomendacion.Habilidad.find_one({'codigo':habilidad})
    if u is not None and h is not  None :
        resu_query =FuncionesNeo4j.VerificarFavorito(usuario=u['codigo'],habilidad=h['codigo'])
    return resu_query




@favorito.get('/deleteFavorito')
async def eliminarFavorito(usuario:str,habilidad:str):
    u=conn.SistemaRecomendacion.Usuario.find_one({'codigo':usuario})
    h=conn.SistemaRecomendacion.Habilidad.find_one({'codigo':habilidad})
    resu_query =FuncionesNeo4j.eliminarFavorito(usuario=u['codigo'],habilidad=h['codigo'])

    return resu_query



@favorito.get('/listarFavoritos')
async def listarFavoritos(usuarios:str):


    resultado=[]

    resu_query =FuncionesNeo4j.listarFavoritos(usuarios=usuarios)


    if(resu_query.empty ):
        return   JSONResponse(status_code=404, content={"message": "false"})
    else:
        mongo = pd.DataFrame(FuncionesMongo.listarHabilidades())
        for i in resu_query.iloc[:,0]:
            comparar = mongo.loc[mongo['codigo'] == i]
            if (len(comparar) > 0):
                comparar = comparar.to_dict('records')
                for s in comparar:
                   resultado.append(s)
        fina=json.dumps(resultado)

        return json.loads(fina)





@favorito.get('/recomendacion')
async def obtenerRecomendacion(codigo:str):

    resultado = []
    resu_query =FuncionesNeo4j.listarRecomendacion(codigo=codigo)
    if resu_query.empty == True:

        #return  JSONResponse(status_code=404, content={"message": "false"})
        return []
    else:
        mongo = pd.DataFrame(FuncionesMongo.listarHabilidades())

        for i in resu_query.iloc[:,0]:
            comparar = mongo.loc[mongo['codigo'] == i]
            if (len(comparar) > 0):
                comparar = comparar.to_dict('records')
                for s in comparar:
                    resultado.append(s)
        fina=json.dumps(resultado)

    return json.loads(fina)





@favorito.get('/pruebaRecomendacion')
async def obtenerPruebaRecomendacion(usuario:str):

    resultado = []
    resu_query =FuncionesNeo4j.querySimilitud(usuario=usuario)
  
 
    if resu_query.empty == True:

       
        return []
    else:
        dato = resu_query.loc[resu_query[2]>0.8]
      
        for i in dato.iloc[:,1]:
            query2=FuncionesNeo4j.listarRecomendacion(codigo=i)
           
      
            for j in query2.iloc[:,0]:
                    mongo = pd.DataFrame(FuncionesMongo.listarHabilidades())
                    comparar = mongo.loc[mongo['codigo'] == j]
                 
                    if (len(comparar) > 0):
                        comparar = comparar.to_dict('records')
                        for s in comparar:
                            if s not in resultado:   
                                resultado.append(s)
            
                
            fina=json.dumps(resultado)

    return json.loads(fina)





@favorito.get('/similitud')
async def algoritmoSimilitud(usuario:str):

    resultado = []
    resu_query =FuncionesNeo4j.querySimilitud(usuario=usuario)
  
 
    if resu_query.empty == True:
        return []
    else:
        dato = resu_query.loc[resu_query[2]>0.9]
      
        for i in dato.iloc[:,1]:
            query2=FuncionesNeo4j.listarRecomendacion2(usuario1='usuario200',usuario2=i)
            if(query2.empty!=True):
                for j in query2.iloc[:,0]:
                    mongo = habilidadEntidad(conn.SistemaRecomendacion.Habilidad.find_one({'codigo':j}))
                   
                    resultado.append(mongo)
                    
    return resultado
