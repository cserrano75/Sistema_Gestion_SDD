from database import engine
from sqlalchemy import text

try:
  with engine.connect() as connection:
    result = connection.execute(text("SELECT version();"))
    print("¡Conexión exitosa a Neon Postgres!")
    print(f"Versión: {result.fetchone()[0]}")
except Exception as e:
  print(f"Error al conectar: {e}")