from pydantic import BaseModel
from typing import Optional

class Competencia(BaseModel):
    id:Optional[str]
    nombre:str
    codigo:str
    codigo_bloque:str