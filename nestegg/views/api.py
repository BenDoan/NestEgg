from flask import *
from util import *
from database import db


api = Blueprint('api', __name__,
                        template_folder='templates')

@api.route("/")
def api_index():
    return "api index"
