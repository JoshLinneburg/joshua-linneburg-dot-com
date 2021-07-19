from flask import Blueprint, render_template, redirect, url_for
from flask_app.models import Post, User, Comment

user_bp = Blueprint("user_bp", __name__)


@user_bp.route("/user/<string:public_user_id>")
def get_user(public_user_id):
    user = User.query.filter_by(public_id=public_user_id).first()

    if not user:
        return redirect(url_for('home_bp.home'))

    posts = Post.query.filter_by(author_id=user.id).all()

    return render_template('user_profile.html', user=user, posts=posts)
