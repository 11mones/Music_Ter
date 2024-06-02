from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    with app.app_context():
        from . import models
        db.create_all()

    return app