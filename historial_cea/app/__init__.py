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

# (Opcional) Aquí irán las importaciones de modelos y vistas en el futuro