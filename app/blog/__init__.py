from flask import Blueprint

blog = Blueprint('blog', __name__)

from app.blog import routes

