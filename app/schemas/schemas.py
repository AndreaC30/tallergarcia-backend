from pydantic import BaseModel, EmailStr
from typing import Optional

# Base del usuario (para registrar y reutilizar)
class UserBase(BaseModel):
    email: EmailStr  # Validación automática de email
    username: str    # 👈 Agregado: ahora todos los usuarios tienen username obligatorio

# Para registrar usuarios (requiere contraseña)
class UserCreate(UserBase):
    password: str

# Para mostrar usuarios sin contraseña
class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True  # 👈 Pydantic v2 reemplaza orm_mode

# Para respuestas con token
class Token(BaseModel):
    access_token: str
    token_type: str

# Para datos dentro del token (ej. usuario autenticado)
class TokenData(BaseModel):
    email: Optional[EmailStr] = None
