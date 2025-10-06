from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from app.db.database import SessionLocal
from app.schemas.schemas import UserCreate, UserOut, Token
from app.crud import crud
from app.auth import auth as auth_utils
from app.auth.security import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from app.auth.auth import get_current_user
from app.models.models import User

router = APIRouter()

# Dependency para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 📌 Endpoint para registrar usuario
@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_email(db, user.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email ya registrado")
    if crud.get_user_by_username(db, user.username):  # ✅ Validación por username
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Nombre de usuario ya en uso")
    return crud.create_user(db, user)

# 🔐 Endpoint para login y generación de token
@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = auth_utils.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales incorrectas")
    token = create_access_token(
        data={"sub": user.email},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)  # ✅ Expiración explícita
    )
    return {"access_token": token, "token_type": "bearer"}

# ✅ Endpoint protegido que devuelve al usuario autenticado
@router.get("/me", response_model=UserOut)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

# 🔒 Ruta solo para administradores
@router.get("/admin-area")
def admin_area(current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tienes permisos de administrador")
    return {"message": f"Bienvenido, admin {current_user.username}"}
