import os

from flask import *
from flask_sqlalchemy import SQLAlchemy

from views import main, api
from database import db
from util import *


app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
    db.init_app(app)
    app.register_blueprint(main, url_prefix='')
    app.register_blueprint(api, url_prefix='/api')
    return app


def setup_database(app):
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    app = create_app()
    if not os.path.isfile('/tmp/test.db'):
      setup_database(app)
    app.run(host="0.0.0.0")
