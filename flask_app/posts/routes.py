from flask import Blueprint, render_template
from flask_app.models import Post

post_bp = Blueprint("post_bp", __name__)


@post_bp.route("/post")
def homepage():
    return render_template("post.html")


@post_bp.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)