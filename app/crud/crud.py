from sqlalchemy.orm import Session
from app.models.models import User
from app.schemas.schemas import UserCreate
from app.auth.security import hash_password

def get_user_by_email(db: Session, email: str) -> User | None:
    """Devuelve un usuario a partir de su email, si existe."""
    return db.query(User).filter(User.email == email).first()

def get_user_by_username(db: Session, username: str) -> User | None:
    """Devuelve un usuario a partir de su nombre de usuario, si existe."""
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate) -> User:
    """Crea un nuevo usuario en la base de datos."""
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
