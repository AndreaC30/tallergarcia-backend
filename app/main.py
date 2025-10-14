# app/main.py

from fastapi import FastAPI
from app.db.database import Base, engine   # ✅ importa Base y engine directamente
from app import models  # importa modelos antes de crear tablas

# ✅ Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

from app.api import routes

app = FastAPI()

# Incluir las rutas
app.include_router(routes.router)

@app.get("/")
def read_root():
    return {"message": "¡Taller García funcionando!"}
