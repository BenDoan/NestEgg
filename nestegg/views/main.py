from flask import *
from util import *
from database import db

INDEX_TPL = load_index()

main = Blueprint('main', __name__,
                        template_folder='templates')

@main.route("/")
def index():
    return INDEX_TPL


@main.route('/<path:path>')
def static_proxy(path):
  return main.send_static_file(path)
