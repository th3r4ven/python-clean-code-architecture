from flask import Flask
from engine.app.repositories.models import db
from engine.app.external.flask.routes import api

app = Flask(__name__)


def create_app():

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    db.init_app(app)
    app.register_blueprint(api, url_prefix="/api")

    return app

