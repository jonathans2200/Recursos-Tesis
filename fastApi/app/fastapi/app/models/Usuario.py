from pydantic import BaseModel
from typing import Optional

class Usuario(BaseModel):
    id:Optional[str]
    codigo:str
    usuario:str
    nombre:str
    apellido:str
    contrasena:str
    correo:str
    rol:str
    
    