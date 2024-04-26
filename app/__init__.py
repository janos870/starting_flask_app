from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    from flask_bootstrap import Bootstrap4
    Bootstrap4(app)

    db.init_app(app)

    from app.account.routes import account
    from app.blog.routes import blog

    app.register_blueprint(account)
    app.register_blueprint(blog)

    from app.account.models import User
    from app.blog.models import Post

    return app












