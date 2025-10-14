# app/models/models.py
from sqlalchemy import Column, Integer, String, Boolean
from app.db.database import Base  # Asegúrate de que este Base es de declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)  # Obligatorio y único
    email = Column(String(100), unique=True, nullable=False, index=True)    # Obligatorio y único
    hashed_password = Column(String(255), nullable=False)                   # Almacena contraseña cifrada
    is_active = Column(Boolean, default=True)                               # Para habilitar/deshabilitar usuario
    is_admin = Column(Boolean, default=False)                               # Para distinguir admins
