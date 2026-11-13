from database.database import SessionLocal
from database.models import Contacto, Proyecto, Responsable, Usuario


def ejecutar_pruebas():
  session = SessionLocal()
  try:
    print("--- 1. PROBANDO ACCESO A USUARIOS ---")
    usuarios = session.query(Usuario).all()
    for u in usuarios:
      print(f"Usuario encontrado: {u.username} (Rol: {u.rol})")

    print("\n--- 2. CONTANDO REGISTROS EN LA NUBE ---")
    total_proyectos = session.query(Proyecto).count()
    total_contactos = session.query(Contacto).count()
    total_responsables = session.query(Responsable).count()

    print(f"Total de Proyectos en Neon: {total_proyectos}")
    print(f"Total de Contactos en Neon: {total_contactos}")
    print(f"Total de Responsables en Neon: {total_responsables}")

    print("\n--- 3. EJEMPLO DE BÚSQUEDA FILTRADA (Primeros 3 proyectos) ---")
    # Buscamos proyectos ordenados por ID
    proyectos_muestra = session.query(Proyecto).limit(3).all()
    for p in proyectos_muestra:
      print(
          f" - Negocio: {p.Negocio} | Cliente: {p.NombreCliente} | Proyecto:"
          f" {p.NombreProyecto}"
      )

    print("\n¡Todas las consultas de prueba se ejecutaron correctamente! 🎉")

  except Exception as e:
    print(f"Ocurrió un error al consultar la base de datos: {e}")
  finally:
    session.close()


if __name__ == "__main__":
  ejecutar_pruebas()