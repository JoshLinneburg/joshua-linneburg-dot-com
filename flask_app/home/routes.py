from flask import Blueprint, render_template, redirect, url_for
from flask_app.models import Post, User

home_bp = Blueprint("home_bp", __name__)


@home_bp.route("/")
def home():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)


@home_bp.route("/about")
def about():
    return render_template("about.html")


@home_bp.route("/contact")
def contact():
    return render_template("contact.html")


@home_bp.route("/user/<string:public_user_id>")
def get_user(public_user_id):
    user = User.query.filter_by(public_id=public_user_id).one()

    if not user:
        return redirect(url_for('home_bp.home'))

    return render_template('user_profile.html', user=user)
