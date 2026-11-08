from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, Text
from sqlalchemy.orm import relationship

# 1. Tabla Participante
class Participante(Model):
    __tablename__ = 'participante'
    id = Column(Integer, primary_key=True)
    ci = Column(String(20), unique=True, nullable=False)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    fecha_nacimiento = Column(Date)
    
    # Relación 1 a N con Inscripcion
    inscripciones = relationship("Inscripcion", back_populates="participante")

    def __repr__(self):
        return f"{self.nombres} {self.apellidos}"

# 2. Tabla Facilitador
class Facilitador(Model):
    __tablename__ = 'facilitador'
    id = Column(Integer, primary_key=True)
    ci = Column(String(20), unique=True, nullable=False)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    especialidad = Column(String(100))
    
    # Relación 1 a N con Taller
    talleres = relationship("Taller", back_populates="facilitador")

    def __repr__(self):
        return f"{self.nombres} {self.apellidos}"

# 3. Tabla Periodo
class Periodo(Model):
    __tablename__ = 'periodo'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False) # Ej: "2026-I"
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)

    def __repr__(self):
        return self.nombre

# 4. Tabla Taller
class Taller(Model):
    __tablename__ = 'taller'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(150), nullable=False)
    carga_horaria = Column(Integer)
    
    # Clave foránea a Facilitador
    facilitador_id = Column(Integer, ForeignKey('facilitador.id'), nullable=False)
    facilitador = relationship("Facilitador", back_populates="talleres")
    
    # Relación 1 a N con Inscripcion
    inscripciones = relationship("Inscripcion", back_populates="taller")

    def __repr__(self):
        return self.nombre

# 5. Tabla Inscripcion
class Inscripcion(Model):
    __tablename__ = 'inscripcion'
    id = Column(Integer, primary_key=True)
    fecha_inscripcion = Column(Date)
    estado = Column(String(50), default='Activo') # Activo, Retirado, Aprobado, Reprobado
    
    # Claves foráneas
    participante_id = Column(Integer, ForeignKey('participante.id'), nullable=False)
    participante = relationship("Participante", back_populates="inscripciones")
    
    taller_id = Column(Integer, ForeignKey('taller.id'), nullable=False)
    taller = relationship("Taller", back_populates="inscripciones")
    
    periodo_id = Column(Integer, ForeignKey('periodo.id'), nullable=False)
    periodo = relationship("Periodo")
    
    # Relación 1 a N con Evaluacion
    evaluaciones = relationship("Evaluacion", back_populates="inscripcion")

    def __repr__(self):
        return f"Inscripción {self.id} - {self.participante}"

# 6. Tabla Evaluacion
class Evaluacion(Model):
    __tablename__ = 'evaluacion'
    id = Column(Integer, primary_key=True)
    tipo_evaluacion = Column(String(50)) # Ej: "Parcial 1", "Proyecto Final"
    nota = Column(Float)
    observaciones = Column(Text)
    
    # Clave foránea a Inscripcion
    inscripcion_id = Column(Integer, ForeignKey('inscripcion.id'), nullable=False)
    inscripcion = relationship("Inscripcion", back_populates="evaluaciones")

    def __repr__(self):
        return f"{self.tipo_evaluacion}: {self.nota}"
