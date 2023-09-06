from pydantic import BaseModel
from typing import Optional

class Encuesta(BaseModel):
    id:Optional[str]
    pregunta1:float
    pregunta2:float
    pregunta3:float
    pregunta4:float

    codigo_usuario:str
    codigo_habilidad:str
    