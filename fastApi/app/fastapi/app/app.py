
from fastapi import FastAPI
from routes.Usuario import usuario
from routes.Area import area
from routes.Bloque import bloque
from routes.Habilidad import habilidad
from routes.Competencia import competencia
from routes.Favorito import favorito
from routes.Links import links
from routes.Encuesta import encuesta

app= FastAPI()
app.include_router(usuario)
app.include_router(area)
app.include_router(bloque)
app.include_router(competencia)
app.include_router(habilidad)
app.include_router(favorito)
app.include_router(links)
app.include_router(encuesta)
