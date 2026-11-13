import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Cargar las variables del archivo .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError(
        "No se encontró la variable de entorno DATABASE_URL en el archivo .env"
    )

# Crear el motor de SQLAlchemy (optimizando para la nube con pool_pre_ping)
engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)

# Fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa para tus modelos ORM
Base = declarative_base()


def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()