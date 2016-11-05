import os

from flask import *
from flask_sqlalchemy import SQLAlchemy

from database import db
from util import *

from views.api import api
from views.main import main


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(main, url_prefix='')
    app.register_blueprint(api, url_prefix='/api')
    return app


def setup_database(app):
    with app.app_context():
        print "Dropping and creating all tables"
        # db.drop_all()
        db.create_all()


if __name__ == '__main__':
    app = create_app()
    setup_database(app)
    app.run(host="0.0.0.0")
