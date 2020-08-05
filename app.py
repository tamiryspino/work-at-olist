from resources.errors import errors
from database.db import initialize_db
from flask import Flask
from flask_mail import Mail
from flask_restful import Api

# imports requiring app and mail
from resources.routes import initialize_routes


app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
mail = Mail(app)


api = Api(app, errors=errors)

initialize_db(app)
initialize_routes(api)
