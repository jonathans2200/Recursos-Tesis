from neo4j import GraphDatabase
from config.db import driver
import pandas as pd




def connection():
   
   driver=GraphDatabase.driver("neo4j://157.230.15.68:7687",
                                auth=("neo4j", 
                                      "Admin12345"))
   return (driver)


      
def listarBloqueArea(codArea):
  driver_neo4j=connection()
  session = driver_neo4j.session()
  query=" Match(n:Bloque) where n.codigo_area='"+str(codArea)+"' return n.codigo as codigo , n.codigo_area as codigo_area"
    
  resultado=session.run(query)
  final =pd.DataFrame(resultado)
  return final
   


  


def listarCompetenciaBloque(codBloque):
  driver_neo4j=connection()
  session = driver_neo4j.session()
  query="Match(n:Competencia) where n.codigo_bloque='"+str(codBloque)+"' return n.codigo as codigo , n.codigo_bloque as codigo_bloque"
    
  resultado=session.run(query)
  return pd.DataFrame(resultado)

def listarHabilidadCompetencia(codCompetencia):
  driver_neo4j=connection()
  session = driver_neo4j.session()
  query="Match(n:Habilidad) where n.codigo_competencia='"+str(codCompetencia)+"' return n.codigo as codigo , n.codigo_competencia as codigo_competencia"
    
  resultado=session.run(query)
  return pd.DataFrame(resultado)


def listarFavoritos(usuarios):
  driver_neo4j=connection()
  session = driver_neo4j.session()
  query=""" 
   MATCH (u:Usuario {codigo: $usuarios})-[r:me_gusta]->(m:Habilidad)
    RETURN m.codigo as codigo
  """
  
  resultado=session.run(query,usuarios=usuarios)
 
  return pd.DataFrame(resultado)






def queryPersona(tx,codigo):
    return tx.run("CREATE (p:Usuario {codigo:$codigo}) RETURN p",
       codigo=codigo).single()

def crearPersona(codigo):
  driver_neo4j=connection()
  session = driver_neo4j.session()

  record = session.execute_write(queryPersona,
                                   codigo=codigo)

  return pd.DataFrame(record)



def queryListFav(tx,usuarios):
    return tx.run(""" 
     MATCH (u:Usuario {codigo: $usuarios})-[r:me_gusta]->(m:Habilidad)
    RETURN m {
        .*,
        favorite: true
    } AS datos
   
    """,
       usuarios=usuarios)

def listvoritos(usuarios):
  driver_neo4j=connection()
  session = driver_neo4j.session()

  record = session.execute_read( queryListFav,
                                   usuarios=usuarios)
  session.close()
  return [row.get('datos') for row in record ] 



def queryFavorito(tx,usuario,habilidad,puntaje):
    return tx.run(""" 
    MATCH (u:Usuario {codigo: $usuario}) 
    MATCH (m:Habilidad {codigo:$habilidad}) 
    MERGE (u)-[r:me_gusta{score:$puntaje}]->(m) RETURN m {favorite: true} AS datos
    """, usuario=usuario,habilidad=habilidad,puntaje=puntaje).single()


def CrearFavorito(usuario,habilidad,puntaje):
  driver_neo4j=connection()
  session = driver_neo4j.session()

  record = session.execute_write(queryFavorito,
                                   usuario=usuario,habilidad=habilidad,puntaje=puntaje)
  
  return record.get('datos')





def queryQuitarFavorito(tx,usuario,habilidad):
  return tx.run("""
   MATCH (u:Usuario {codigo: $usuario})-[r:me_gusta]->(m:Habilidad {codigo:$habilidad})
            DELETE r
            RETURN m {
                message: false
            } AS datos
  
  """, usuario=usuario,habilidad=habilidad).single()


def eliminarFavorito(usuario,habilidad):
  driver_neo4j=connection()
  session = driver_neo4j.session()

  record = session.execute_write(queryQuitarFavorito,
                                   usuario=usuario,habilidad=habilidad)

  return record.get('datos')








def listarRecomendacion(codigo):
  driver_neo4j=connection()
  session = driver_neo4j.session()
  query=""" 
   MATCH (p1:Usuario)-[:me_gusta]->(b1:Habilidad)<-[:me_gusta]-(p2:Usuario)-[:me_gusta]->(b2:Habilidad)
WHERE  b1.codigo<>b2.codigo and p1.codigo='"""+str(codigo)+"""'
RETURN  b2.codigo as HabilidadRecomendada
Limit 5
  """
  
  resultado=session.run(query)

  return pd.DataFrame(resultado)



def listarRecomendacion2(usuario1,usuario2):
  driver_neo4j=connection()
  session = driver_neo4j.session()
  query=""" 
  MATCH (p1:Usuario)-[:me_gusta]->(b1:Habilidad)<-[:me_gusta]-(p2:Usuario)-[:me_gusta]->(b2:Habilidad)
WHERE   b1.codigo<>b2.codigo and p1.codigo='"""+str(usuario1)+"""' and p2.codigo='"""+str(usuario2)+"""'  and b1.codigo_competencia=b2.codigo_competencia 
RETURN  b2.codigo as HabilidadRecomendada

  """
  
  resultado=session.run(query)
  final =pd.DataFrame(resultado) 
 # print(final.dropna)
  return final.dropna()


def queryVerificar(tx,usuario,habilidad):
    return tx.run(""" 
    
   MATCH (Usuario{codigo: $usuario})-[:me_gusta]->(h:Habilidad{codigo:$habilidad}) RETURN count(h) as datos
    """, usuario=usuario,habilidad=habilidad).single()


def VerificarFavorito(usuario,habilidad):
  driver_neo4j=connection()
  session = driver_neo4j.session()
  
  
  record = session.execute_write(queryVerificar,
                                   usuario=usuario,habilidad=habilidad)

  if record.get('datos')>0:
     return {'estado':'True'}
  else:
     return {'estado':'False'}
     
  







  
def querySimilitud(usuario):
  driver_neo4j=connection()
  session = driver_neo4j.session()
  query=""" 
  MATCH (p1:Usuario {codigo:'"""+str(usuario)+"""'})-[likes1:me_gusta]->(cuisine)
  MATCH (p2:Usuario)-[likes2:me_gusta]->(cuisine2) where p1<>p2
  WITH p1, collect(likes1.score) AS p1L, p2, collect(likes2.score) AS p2L
  RETURN p1.codigo AS Usuario, p2.codigo AS Usuarios,
   gds.similarity.cosine(p1L, p2L) AS similitud ORDER BY similitud DESCENDING
  limit 5
  
  """
  
  resultado=session.run(query)
  return pd.DataFrame(resultado)