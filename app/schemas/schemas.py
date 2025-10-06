from pydantic import BaseModel, EmailStr
from typing import Optional


# Base del usuario (para registrar y reutilizar)
class UserBase(BaseModel):
    email: EmailStr  # Validación de correo automático
    full_name: Optional[str] = None


# Para registrar usuarios (requiere contraseña)
class UserCreate(UserBase):
    password: str


# Para mostrar usuarios sin contraseña
class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True


# Para respuestas con token
class Token(BaseModel):
    access_token: str
    token_type: str


# Para datos dentro del token (ej. usuario autenticado)
class TokenData(BaseModel):
    email: Optional[EmailStr] = None
