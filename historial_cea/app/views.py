from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.actions import action
from flask import flash, redirect
from app.models import Participante, Facilitador, Periodo, Taller, Inscripcion, Evaluacion
from app.ia_service import generar_comentario_ia

class ParticipanteView(ModelView):
    datamodel = SQLAInterface(Participante)
    list_columns = ['ci', 'nombres', 'apellidos']

    @action("ia_reporte", "Generar Reporte IA", "Analizar rendimiento con IA", "fa-magic", single=True)
    def ia_reporte(self, items):
        participante = items[0]
        inscripciones = self.datamodel.session.query(Inscripcion).filter(Inscripcion.participante_id == participante.id).all()
        notas = []
        taller_nombre = "General"
        
        for ins in inscripciones:
            if ins.evaluaciones:
                taller_nombre = ins.taller.nombre
                for ev in ins.evaluaciones:
                    notas.append(ev.nota)
        
        if not notas:
            flash(f"El participante {participante.nombres} aún no tiene notas registradas para analizar.", "warning")
            return redirect(self.get_redirect())

        comentario = generar_comentario_ia(participante.nombres, notas, taller_nombre)
        flash(f"Análisis de IA para {participante.nombres}: {comentario}", "info")
        return redirect(self.get_redirect())

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