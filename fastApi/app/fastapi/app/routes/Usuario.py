from fastapi import APIRouter,HTTPException
from fastapi.responses import JSONResponse

from config.db import conn
from schemas.usuario import usuarioEntidad,usuariosEntidad
from models.Usuario import Usuario
from funciones import FuncionesNeo4j,FuncionesMongo
from bson import ObjectId
from passlib.hash import sha256_crypt
usuario=APIRouter()

@usuario.get('/usuarios',response_model=list[Usuario])
async def listarUsuario():
    return usuariosEntidad(conn.SistemaRecomendacion.Usuario.find())

@usuario.post('/addUsuario')
async def crearUsuario(usuario:str,contrasena:str,correo:str,rol:str,nombre:str,apellido:str):
    nuevoUsuario={"codigo":usuario,"usuario":usuario,'nombre':nombre,'apellido':apellido,"contrasena":contrasena,"correo":correo,"rol":rol}
  
    id = conn.SistemaRecomendacion.Usuario.insert_one(nuevoUsuario).inserted_id
 
    usuario=conn.SistemaRecomendacion.Usuario.find_one({'_id':id})
    FuncionesNeo4j.crearPersona(codigo=str(usuario['codigo']))
    return usuarioEntidad(usuario)    

@usuario.get('/usuarios/{codigo}',response_model=Usuario)
async def buscarUsuario(codigo:str):
   
    return usuarioEntidad( conn.SistemaRecomendacion.Usuario.find_one({'_id':ObjectId(codigo)}))




@usuario.post('/login')
async def validadUsuario(usuario:str,contrasena:str):
    
    dato = conn.SistemaRecomendacion.Usuario.find_one({'usuario':usuario,'contrasena':contrasena})
    
    if dato:
        return  JSONResponse(status_code=200, content={'data':usuarioEntidad(dato),'mensaje':''})
      
    #    return JSONResponse(status_code=200, content=usuarioEntidad(dato))
    else :
         return  JSONResponse(status_code=200, content={'data':{
   
    "codigo": "",
    "usuario": "",
     "nombre": "",
      "apellido": "",
    "contrasena": "",
    "correo": "",
    "rol": " "
  },'mensaje':'Credenciales Incorrectas'})
    #     #return JSONResponse(status_code=401, content={'mensaje':"Credenciales incorrectas"})
  


@usuario.get('/findUser')
async def findUsuario(codigo:str):

    return usuarioEntidad(conn.SistemaRecomendacion.Usuario.find_one({'codigo':codigo}))
    
@usuario.put('/updateUser')
async def editarUsuario(usuario:str,nombre:str,apellido:str,contrasena:str,correo:str):
    conn.SistemaRecomendacion.Usuario.update_one({'usuario':usuario},{'$set':{'contrasena':contrasena,'correo':correo,'nombre':nombre,'apellido':apellido}})
    dato=conn.SistemaRecomendacion.Usuario.find_one({'usuario':usuario})

    return  JSONResponse(status_code=200, content=usuarioEntidad(dato))





@usuario.get('/validarUsuario')
async def verificacionUsuario(palabra:str):
    return usuariosEntidad(conn.SistemaRecomendacion.Usuario.find({"usuario":{"$regex":'^'+ palabra+'$', "$options": "m"}}).limit(1))

