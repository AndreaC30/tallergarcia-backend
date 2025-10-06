# app/create_admin.py

from app.db.database import SessionLocal
from app.models.models import User
from app.auth.security import hash_password

# Datos del usuario administrador
ADMIN_USERNAME = "admin"
ADMIN_EMAIL = "admin@example.com"
ADMIN_PASSWORD = "admin123"  # Cambia esto por algo seguro

# Inicializar sesión
db = SessionLocal()

# Verificar si ya existe
existing = db.query(User).filter(
    (User.username == ADMIN_USERNAME) | (User.email == ADMIN_EMAIL)
).first()

if existing:
    print("❌ Ya existe un usuario con ese email o username.")
else:
    # Crear nuevo admin
    admin = User(
        username=ADMIN_USERNAME,
        email=ADMIN_EMAIL,
        hashed_password=hash_password(ADMIN_PASSWORD),
        is_active=True,
        is_admin=True
    )
    db.add(admin)
    db.commit()
    print("✅ Usuario administrador creado correctamente.")

db.close()
