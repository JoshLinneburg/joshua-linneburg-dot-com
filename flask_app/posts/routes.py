from flask import Blueprint, render_template

post_bp = Blueprint("post_bp", __name__)


@post_bp.route("/post")
def homepage():
    return render_template("post.html")
