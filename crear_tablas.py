from database import Base, engine
# Importamos los modelos para que SQLAlchemy los reconozca
from models import Contacto, Proyecto, Responsable, Usuario

print("Conectando a Neon y creando tablas...")
Base.metadata.create_all(bind=engine)
print("¡Tablas creadas exitosamente en Neon!")