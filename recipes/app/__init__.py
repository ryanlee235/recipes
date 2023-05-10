import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .extensions import db
from .views import bp


def create_app():
    basedir = os.path.abspath(os.path.dirname(__file__))
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'recipes'
    app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
    
    db.init_app(app)
    app.register_blueprint(bp)
    with app.app_context():
        db.create_all()
        
    return app