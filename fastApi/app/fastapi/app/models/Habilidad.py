from pydantic import BaseModel
from typing import Optional

class Habilidad(BaseModel):
    id:Optional[str]
    codigo:str
    cod_competencia:str
    identificador:str
    nombre:str
    
