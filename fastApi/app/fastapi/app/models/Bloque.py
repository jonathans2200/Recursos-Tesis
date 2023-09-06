from pydantic import BaseModel
from typing import Optional

class Bloque(BaseModel):
    id:Optional[str]
    nombre:str
    codigo:str
    codigo_area:str