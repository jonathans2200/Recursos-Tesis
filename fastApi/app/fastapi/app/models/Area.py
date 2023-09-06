from pydantic import BaseModel
from typing import Optional

class Area(BaseModel):
    id:Optional[str]
    nombre:str
    codigo:str
    imagen:str
    
