from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from app.models import Participante, Facilitador, Periodo, Taller, Inscripcion, Evaluacion

class ParticipanteView(ModelView):
    datamodel = SQLAInterface(Participante)
    list_columns = ['ci', 'nombres', 'apellidos']

class FacilitadorView(ModelView):
    datamodel = SQLAInterface(Facilitador)
    list_columns = ['ci', 'nombres', 'apellidos', 'especialidad']

class PeriodoView(ModelView):
    datamodel = SQLAInterface(Periodo)
    list_columns = ['nombre', 'fecha_inicio', 'fecha_fin']

class TallerView(ModelView):
    datamodel = SQLAInterface(Taller)
    list_columns = ['nombre', 'carga_horaria', 'facilitador']

class InscripcionView(ModelView):
    datamodel = SQLAInterface(Inscripcion)
    list_columns = ['participante', 'taller', 'periodo', 'estado']

class EvaluacionView(ModelView):
    datamodel = SQLAInterface(Evaluacion)
    list_columns = ['inscripcion', 'tipo_evaluacion', 'nota']