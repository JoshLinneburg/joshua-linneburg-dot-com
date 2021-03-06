import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost/joshua-linneburg-dot-com"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://") if os.environ.get('DATABASE_URL') else 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    LANGUAGES = ['en', 'es']
    POSTS_PER_PAGE = 25
    TEMPLATE_AUTO_RELOAD = True
