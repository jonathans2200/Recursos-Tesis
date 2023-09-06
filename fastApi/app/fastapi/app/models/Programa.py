from pydantic import BaseModel
from typing import Optional

class Programa(BaseModel):
    id:Optional[str]
    identificador:str
    link:str
    codigo:str
    descripcion:str
    nombre:str
    item:str
    
