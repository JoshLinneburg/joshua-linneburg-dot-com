import uuid
from flask import Blueprint, render_template, request
from flask_app.models import Post, PostTag, Tag
from flask_app import db

post_bp = Blueprint("post_bp", __name__)


@post_bp.route("/post")
def get_all_posts():
    posts = Post.query.order_by(Post.created_datetime.desc()).all()

    return render_template("posts/post_directory.html", posts=posts)


@post_bp.route('/post/<string:post_public_id>')
def get_post(post_public_id):
    post = Post.query.filter_by(public_id=post_public_id).one()

    return render_template('posts/post.html', post=post)


@post_bp.route("/post", methods=["POST"])
def add_post():
    data = request.get_json()

    new_post = Post(
        public_id=str(uuid.uuid4()),
        title=data["title"],
        subtitle=data["subtitle"],
        body=data["body"],
        author_id=data["author_id"]
    )

    db.session.add(new_post)
    db.session.commit()

    return {
        "message": "Created!",
        "status_code": 201,
        "status_text": "OK!"
    }


@post_bp.route('/tag/<string:tag_public_id>')
def get_posts_by_tag(tag_public_id):

    tag = Tag.query.filter_by(public_id=tag_public_id).first()

    posts = Post.query.join(PostTag).filter_by(tag_id=tag.id).all()

    return render_template('posts/post_directory.html', posts=posts)
