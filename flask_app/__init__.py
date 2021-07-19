import markdown.extensions.fenced_code

from flask import Flask
from flask_bootstrap import Bootstrap
# from errors.handlers import jwt
from flask_migrate import Migrate
from flask_cors import CORS
from flask_login import LoginManager
from flaskext.markdown import Markdown
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flasgger import Swagger
from flask_app.utils import datetime_filter

bootstrap = Bootstrap()
db = SQLAlchemy()
login = LoginManager()
migrate = Migrate()
cors = CORS()
swag = Swagger()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    bootstrap.init_app(app=app)
    db.init_app(app=app)
    login.init_app(app=app)
    md = Markdown(app=app, auto_escape=True, extensions=["fenced_code"])
    migrate.init_app(app=app, db=db)
    # jwt.init_app(app=app)
    cors.init_app(app=app)
    swag.init_app(app=app)

    from .home.routes import home_bp
    app.register_blueprint(home_bp)

    from .posts.routes import post_bp
    app.register_blueprint(post_bp)

    from .auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    from .users.routes import user_bp
    app.register_blueprint(user_bp)

    app.jinja_env.filters["datetime_filter"] = datetime_filter

    return app


from flask_app.models import *
