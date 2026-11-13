from database import Base
from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, Text


class Usuario(Base):
  __tablename__ = "usuarios"

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, nullable=False, unique=True)
  password_hash = Column(String, nullable=False)
  rol = Column(String, nullable=True)
  activo = Column(Boolean, nullable=True)


class Responsable(Base):
  __tablename__ = "responsables"

  Id_Responsable = Column(
      Integer, primary_key=True, index=True
  )  # Mapeado desde bigint
  Nombre_Responsable = Column(Text, nullable=True)
  Cargo_Responsable = Column(Text, nullable=True)
  Iniciales = Column(Text, nullable=True)
  Area = Column(Integer, nullable=True)


class Contacto(Base):
  __tablename__ = "contactos"

  # Como no viene una llave primaria explícita en el listado, agregamos un ID autoincremental de respaldo
  id = Column(Integer, primary_key=True, autoincrement=True)
  Cliente = Column(Text, nullable=True)
  Nombre = Column(Text, nullable=True)
  Cargo = Column(Text, nullable=True)
  Telefono = Column(Text, nullable=True)
  Fax = Column(Text, nullable=True)
  Celular = Column(Text, nullable=True)
  Mail = Column(Text, nullable=True)
  idJerarquia = Column(Float, nullable=True)


class Proyecto(Base):
  __tablename__ = "proyectos"

  # Llave primaria autoincremental de control para SQLAlchemy
  id = Column(Integer, primary_key=True, autoincrement=True)
  Negocio = Column(Text, nullable=True)
  Correlativo = Column(Float, nullable=True)
  NombreCliente = Column(Text, nullable=True)
  NombreProyecto = Column(Text, nullable=True)
  Mandante = Column(Text, nullable=True)
  Destino = Column(Text, nullable=True)
  Prioridad = Column(Float, nullable=True)
  Rubro = Column(Text, nullable=True)
  Industria = Column(Text, nullable=True)
  PesoTM = Column(Float, nullable=True)
  Status = Column(Text, nullable=True)
  Notas = Column(Text, nullable=True)
  FechaRecepcion = Column(DateTime, nullable=True)
  FechaPresentacion = Column(DateTime, nullable=True)
  semanaentregacotizacion = Column(Text, nullable=True)
  InicioEntregas = Column(DateTime, nullable=True)
  MesCierre = Column(Text, nullable=True)
  agnocierre = Column(Float, nullable=True)
  OT = Column(Text, nullable=True)
  Margen = Column(Float, nullable=True)
  PU = Column(Float, nullable=True)
  COU = Column(Text, nullable=True)
  VOU = Column(Text, nullable=True)
  MO = Column(Text, nullable=True)
  Dolar = Column(Text, nullable=True)
  Ubicacion = Column(Text, nullable=True)
  TipoContrato = Column(Text, nullable=True)
  Mes = Column(DateTime, nullable=True)
  Responsable = Column(Text, nullable=True)
  TipoCotizacion = Column(Text, nullable=True)
  ADC = Column(Text, nullable=True)
  Ingenieria = Column(Text, nullable=True)
  TMFinal = Column(Float, nullable=True)
  PVFinal = Column(Float, nullable=True)
  CostoSumi = Column(Float, nullable=True)
  CostoDir = Column(Float, nullable=True)
  CostoIndir = Column(Float, nullable=True)
  MargenUF = Column(Float, nullable=True)
  MargenPorc = Column(Float, nullable=True)
  SubSector = Column(Text, nullable=True)
  Encuesta = Column(Boolean, nullable=True)
  Negociacion = Column(Boolean, nullable=True)
  FechaAdjudicacion = Column(DateTime, nullable=True)
  FechaEntregas = Column(Text, nullable=True)
  PreAdj = Column(Boolean, nullable=True)
  Presupuesto = Column(Text, nullable=True)
  Distribucion = Column(Text, nullable=True)
  StatusDistr = Column(Text, nullable=True)
  Maestranza = Column(Text, nullable=True)
  OpFabricacion = Column(Boolean, nullable=True)
  OpMontaje = Column(Boolean, nullable=True)
  Ambito = Column(Float, nullable=True)
  PptoEstimado = Column(Float, nullable=True)
  ProbExito = Column(Float, nullable=True)
  Comodin1 = Column(Text, nullable=True)
  Comodin2 = Column(Text, nullable=True)
  Comodin3 = Column(Boolean, nullable=True)
  Comodin4 = Column(Text, nullable=True)
  PercMC = Column(Float, nullable=True)
  ValorMC = Column(Float, nullable=True)