from flask.cli import FlaskGroup
from flask_app import create_app, db
from flask_app.models import User, Post, Comment, Tag, PostTag

app = create_app()
cli = FlaskGroup(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Tag': Tag,
            'Comment': Comment, 'PostTag': PostTag}
