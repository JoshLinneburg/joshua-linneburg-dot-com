from flask import Blueprint, render_template
from flask_app.models import Post

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
