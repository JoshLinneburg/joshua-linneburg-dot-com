from flask import Flask
# from errors.handlers import jwt
from flask_migrate import Migrate
from flask_cors import CORS
from flask_login import LoginManager
from flaskext.markdown import Markdown
import markdown.extensions.fenced_code
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flasgger import Swagger

db = SQLAlchemy()
# login = LoginManager()
migrate = Migrate()
cors = CORS()
swag = Swagger()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app=app)
    # login.init_app(app=app)
    md = Markdown(app=app, auto_escape=True, extensions=["fenced_code"])
    migrate.init_app(app=app, db=db)
    # jwt.init_app(app=app)
    cors.init_app(app=app)
    swag.init_app(app=app)

    from .home.routes import home_bp
    app.register_blueprint(home_bp)

    from .posts.routes import post_bp
    app.register_blueprint(post_bp)

    return app


from flask_app.models import *
