import uuid
from flask import Blueprint, render_template, request
from flask_app import db
from flask_app.models import Post, PostTag, Tag
from flask_app.posts.forms import PostForm
from flask_app.errors.handlers import not_found_error, internal_error
from flask_login import current_user, login_required
from sqlalchemy.orm.exc import NoResultFound

post_bp = Blueprint("post_bp", __name__)


@post_bp.route("/posts", methods=["GET"])
def get_all_posts():
    posts = Post.query.order_by(Post.created_datetime.desc()).all()

    return render_template("posts/post_directory_page.html", posts=posts)


@post_bp.route('/post/<string:post_public_id>', methods=["GET"])
def get_post(post_public_id):
    try:
        post = Post.query.filter_by(public_id=post_public_id).one()
        return render_template('posts/post.html', post=post)

    except NoResultFound as e:
        return not_found_error("No post found with that public ID.")


@post_bp.route("/post", methods=["GET", "POST"])
@login_required
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(
            public_id=str(uuid.uuid4()),
            body=form.data["body"],
            title=form.data["title"],
            subtitle=form.data["subtitle"],
            author_id=current_user.get_id()
        )

        db.session.add(new_post)

        try:
            tags = []
            for tag in form.data["tags"]:
                tags.append(Tag.query.filter_by(tag_name=tag).one())
        except NoResultFound as e:
            return not_found_error(f"Could not find tag: {tag} to attach to post.")

        new_post.tags = tags

        db.session.add(new_post)
        db.session.commit()

        return render_template('posts/post.html', post=new_post)

    form.tags.choices = [(tag.tag_name, tag.tag_name) for tag in Tag.query.all()]
    return render_template("posts/add_post.html", form=form)


@post_bp.route('/tag/<string:tag_public_id>')
def get_posts_by_tag(tag_public_id):
    try:
        tag = Tag.query.filter_by(public_id=tag_public_id).one()

        posts = Post.query.join(PostTag).filter_by(tag_id=tag.id).all()

        return render_template('posts/post_directory_page.html', posts=posts, tag=tag)

    except NoResultFound as e:
        return not_found_error("Could not find a tag that matched your query.")
