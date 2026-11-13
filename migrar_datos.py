import os
from database.database import SessionLocal  # Esta es tu conexión a Neon ya configurada
from database.models import Contacto, Proyecto, Responsable, Usuario
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# --- CONFIGURA TU CONEXIÓN LOCAL AQUÍ ---
# Reemplaza 'postgres', 'tu_password', 'localhost:5432' y 'CRM-Ventas' según corresponda
LOCAL_DATABASE_URL = (
    "postgresql://postgres:Asus2026@localhost:5432/CRM-Ventas"
)

local_engine = create_engine(LOCAL_DATABASE_URL)
LocalSession = sessionmaker(bind=local_engine)


def migrar_tabla(nombre_tabla, modelo_clase):
  print(f"Migrando tabla: {nombre_tabla}...")
  local_session = LocalSession()
  neon_session = SessionLocal()

  try:
    # 1. Leer todos los registros de la base de datos local usando SQL directo o el modelo
    # Para hacerlo genérico y seguro frente a diferencias de IDs, leemos las filas como diccionarios
    from sqlalchemy import text

    resultado = local_session.execute(
        text(f"SELECT * FROM {nombre_tabla}")
    ).mappings().all()

    if not resultado:
      print(f"  -> La tabla {nombre_tabla} está vacía en local. Saltando...")
      return

    contador = 0
    for fila in resultado:
      # Convertimos el row mapping a diccionario, excluyendo la columna 'id' autoincremental si choca
      datos_fila = dict(fila)

      # Si la tabla usa un id autoincremental que manejaremos automáticamente, puedes removerlo si da conflicto:
      # if 'id' in datos_fila: del datos_fila['id']

      # Creamos la instancia del modelo para Neon
      registro = modelo_clase(**datos_fila)
      neon_session.add(registro)
      contador += 1

    neon_session.commit()
    print(
        f"  -> ¡{contador} registros migrados con éxito en '{nombre_tabla}'!"
    )

  except Exception as e:
    neon_session.rollback()
    print(f"  -> Error migrando {nombre_tabla}: {e}")
  finally:
    local_session.close()
    neon_session.close()


if __name__ == "__main__":
  print("Iniciando proceso de migración hacia Neon...")

  # Orden de migración (puedes ajustar según tus tablas)
  migrar_tabla("usuarios", Usuario)
  migrar_tabla("responsables", Responsable)
  migrar_tabla("contactos", Contacto)
  migrar_tabla("proyectos", Proyecto)

  print("¡Proceso de migración finalizado!")