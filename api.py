from flask.cli import FlaskGroup
from app import create_app, db
from app.models import User, Post, Comment, Tag, PostTag

app = create_app()
cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Tag': Tag,
            'Comment': Comment, 'PostTag': PostTag}
