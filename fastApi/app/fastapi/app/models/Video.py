from pydantic import BaseModel
from typing import Optional

class Video(BaseModel):
    id:Optional[str]
    identificador:int
    codigo:str
    link:str
    descripcion:str
    
