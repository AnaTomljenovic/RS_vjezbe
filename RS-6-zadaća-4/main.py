from fastapi import FastAPI
from routers import filmovi

app = FastAPI()

# Uključivanje ruta za filmove
app.include_router(filmovi.router, tags=["Filmovi"], prefix="/api")
