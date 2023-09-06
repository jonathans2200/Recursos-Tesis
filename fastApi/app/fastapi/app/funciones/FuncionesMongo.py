from config.db import conn
from schemas.area import areasEntidad
from schemas.bloque import bloqueEntidad
import pandas as pd

def listarBloqueAreaM(codArea):
  datos=pd.DataFrame(list(conn.SistemaRecomendacion.Bloque.find({"codigo_area": codArea},{'_id':False})))
  return  datos

def listarCompetenciaBloque(codBloque):
    datos=pd.DataFrame(list(conn.SistemaRecomendacion.Competencia.find({"codigo_bloque": codBloque},{'_id':False})))
    return datos

def listarHabilidadCompetencia(codCompetencia):
    datos=pd.DataFrame(list(conn.SistemaRecomendacion.Habilidad.find({"cod_competencia": codCompetencia},{'_id':False})))
    return datos    

def buscadorHabilidad(palabra):
  datos=pd.DataFrame(list(conn.SistemaRecomendacion.Habilidad.find({ "nombre":'/'+palabra+'/i'  })))
  return datos
def listarHabilidades():
    datos=pd.DataFrame(list(conn.SistemaRecomendacion.Habilidad.find({},{'_id':False})))
 
    return datos 

def listarHabilidades2(codigo):
    datos=pd.DataFrame(list(conn.SistemaRecomendacion.Habilidad.find_one({'codigo':codigo},{'_id':False})))

    return datos 
