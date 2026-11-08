from flask import render_template, request
from flask_appbuilder import BaseView, expose
from app.models import Participante, Evaluacion, Inscripcion, Taller

class ReportesView(BaseView):
    route_base = "/reportes"
    default_view = "index"

    @expose("/")
    def index(self):
        return render_template("reportes/index.html")

    # REPORTE 1: Historial por estudiante (Filtro: ID del participante)
    @expose("/historial")
    def historial(self):
        participante_id = request.args.get('participante_id')
        datos = []
        participante = None
        if participante_id:
            participante = self.appbuilder.get_session.query(Participante).get(participante_id)
            datos = self.appbuilder.get_session.query(Evaluacion).join(Inscripcion).filter(Inscripcion.participante_id == participante_id).all()
        participantes = self.appbuilder.get_session.query(Participante).all()
        return render_template("reportes/historial.html", datos=datos, participantes=participantes, participante=participante)

    # REPORTE 2: Promedio por taller
    @expose("/promedios")
    def promedios(self):
        from sqlalchemy import func
        datos = self.appbuilder.get_session.query(
            Taller.nombre, 
            func.avg(Evaluacion.nota).label('promedio')
        ).join(Inscripcion, Taller.id == Inscripcion.taller_id)\
         .join(Evaluacion, Inscripcion.id == Evaluacion.inscripcion_id)\
         .group_by(Taller.nombre).all()
        return render_template("reportes/promedios.html", datos=datos)

    # REPORTE 3: Aprobados y Reprobados
    @expose("/aprobados")
    def aprobados(self):
        from sqlalchemy import func
        datos = self.appbuilder.get_session.query(
            Participante.nombres, 
            Participante.apellidos,
            func.avg(Evaluacion.nota).label('promedio')
        ).join(Inscripcion, Participante.id == Inscripcion.participante_id)\
         .join(Evaluacion, Inscripcion.id == Evaluacion.inscripcion_id)\
         .group_by(Participante.id).all()
        return render_template("reportes/aprobados.html", datos=datos)