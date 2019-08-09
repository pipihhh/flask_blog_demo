from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = Flask(__name__)


from demo import models
from demo.views.login.login import lg


def create_app():
    app.config.from_object("demo.settings.DebugConfig")
    db.init_app(app)
    app.register_blueprint(lg)
    return app
