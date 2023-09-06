from pydantic import BaseModel
from typing import Optional
from models.Usuario import  Usuario

class UsuarioData(BaseModel):
    user:Optional[Usuario]
    mensaje:str
    