from flask import Flask
from flask_appbuilder import AppBuilder, SQLA

# 1. Creamos la app de Flask y cargamos la configuración
app = Flask(__name__)
app.config.from_object('config')

# 2. Inicializamos SQLA con la app directamente
db = SQLA(app)

# 3. Inicializamos AppBuilder
appbuilder = AppBuilder(app, db.session)

# 4. Empujamos el contexto para que los comandos de la terminal funcionen
app.app_context().push()

# Importar las vistas para que aparezcan en el menú
from app.views import ParticipanteView, FacilitadorView, PeriodoView, TallerView, InscripcionView, EvaluacionView

appbuilder.add_view(ParticipanteView, "Participantes", category="Gestión CEA", icon="fa-users")
appbuilder.add_view(FacilitadorView, "Facilitadores", category="Gestión CEA", icon="fa-chalkboard-teacher")
appbuilder.add_view(PeriodoView, "Periodos", category="Gestión CEA", icon="fa-calendar")
appbuilder.add_view(TallerView, "Talleres", category="Gestión CEA", icon="fa-book")
appbuilder.add_view(InscripcionView, "Inscripciones", category="Gestión CEA", icon="fa-file-signature")
appbuilder.add_view(EvaluacionView, "Evaluaciones", category="Gestión CEA", icon="fa-star")
from app.reports import ReportesView
appbuilder.add_view(ReportesView, "Reportes", category="Gestión CEA", icon="fa-chart-bar")