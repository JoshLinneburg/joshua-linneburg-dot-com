from flask import Blueprint, render_template
from flask_app import db

error_bp = Blueprint('error_bp', __name__)


@error_bp.app_errorhandler(404)
def not_found_error(error=None):
    return render_template('errors/404.html', error=error), 404


@error_bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html', error=error), 500