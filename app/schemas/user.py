from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# ✅ Esquema para crear un nuevo usuario (registro)
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)

# ✅ Esquema de respuesta de usuario (sin contraseña)
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool = True
    is_admin: bool = False

    class Config:
        from_attributes = True  # Para que funcione con ORM (Pydantic v2)
