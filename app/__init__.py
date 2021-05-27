from flask import Flask
from errors.handlers import jwt
from flask_migrate import Migrate
from flask_cors import CORS
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config
from flasgger import Swagger

db = SQLAlchemy()
ma = Marshmallow()
login = LoginManager()
migrate = Migrate()
cors = CORS()
swag = Swagger()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app=app)
    ma.init_app(app=app)
    login.init_app(app=app)
    migrate.init_app(app=app, db=db)
    jwt.init_app(app=app)
    cors.init_app(app=app)
    swag.init_app(app=app)

    from .home.routes import home_bp
    app.register_blueprint(home_bp)

    return app


from app.models import *
