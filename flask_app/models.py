import base64
import json
import jwt
import os

from flask_app import db
from datetime import datetime, timedelta
from flask import current_app, url_for
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(128), unique=True)
    profile_picture_path = db.Column(db.String(128))
    email = db.Column(db.String(50), unique=True)
    phone_nbr = db.Column(db.String(15), unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    posts = db.relationship("Post", backref="author", lazy="dynamic")
    comments = db.relationship("Comment", backref="author", lazy="dynamic")
    created_datetime = db.Column(db.DateTime, default=datetime.utcnow)
    modified_datetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def set_password(self, password):
        """
        Sets the password of the User to the password passed in.
        Args:
            password: str
                A str containing the User's new password.
        Returns:
            None.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Checks the hash of a User's password against the hash of a password they've
        provided for authentication.
        Args:
            password: str
                A str containing the password the User wants to authenticate with.
        Returns:
            result: bool
                Whether the password the User provided matches the
                password associated with their account.
        """
        result = check_password_hash(self.password_hash, password)
        return result


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(128), unique=True)
    body = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    comments = db.relationship("Comment", backref="post", lazy="dynamic")
    created_datetime = db.Column(db.DateTime, default=datetime.utcnow)
    modified_datetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(128), unique=True)
    tag_name = db.Column(db.String(64), unique=True)
    created_datetime = db.Column(db.DateTime, default=datetime.utcnow)
    modified_datetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class PostTag(db.Model):
    post_id = db.Column(db.Integer, db.ForeignKey("post.id", ondelete="CASCADE"), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id", ondelete="CASCADE"), primary_key=True)
    created_datetime = db.Column(db.DateTime, default=datetime.utcnow)
    modified_datetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(128), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
    body = db.Column(db.Text)
    created_datetime = db.Column(db.DateTime, default=datetime.utcnow)
    modified_datetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
