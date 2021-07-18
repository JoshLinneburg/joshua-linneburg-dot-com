from flask import Blueprint, render_template
from flask_app.models import Post

post_bp = Blueprint("post_bp", __name__)


@post_bp.route("/post")
def get_all_posts():
    posts = Post.query.all()
    return render_template("post_directory.html", posts=posts)


@post_bp.route('/post/<int:post_id>')
def get_post(post_id):
    post = Post.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)


@post_bp.route("/post/add")
def add_post():
    return render_template("add.html")