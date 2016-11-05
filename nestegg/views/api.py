import calendar
import json

from flask import Blueprint, request
from util import *
from consts import *
from database import db, Budget, Bucket, BudgetItem

api = Blueprint('api', __name__,
                        template_folder='templates')

@api.route("/", methods=['POST', "GET"])
def hello():
    return "Hello"

@api.route("/budget/create", methods=['POST'])
def budget_create():
    budget_dict = request.get_json()

    budget = Budget()
    budget.year = int(budget_dict['year'])
    budget.month = month_name_to_num(budget_dict['month'])
    db.session.add(budget)

    for cat_name, sub_cat in budget_dict['items'].items():
        for sub_cat_name, attrs in sub_cat.items():
            i = BudgetItem()
            i.budget = budget
            i.sub_category = sub_cat_name
            i.category = cat_name
            i.max = attrs['max']
            i.type = attrs['type']

            if attrs['type'] == BUDGET_TYPES['bucket']:
                bucket = Bucket(attrs['bucket'], budget)
                db.session.add(bucket)

                i.bucket = bucket

            db.session.add(i)
    db.session.commit()

    return "Good"

@api.route("/budget/get/<year>/<month>", methods=['GET'])
def budget_get(year, month):
    budget = Budget.query.filter_by(year=int(year), month=month_name_to_num(month)).first_or_404()
    budget_items = BudgetItem.query.filter_by(budget=budget).all()

    # import IPython; IPython.embed()
    budget_ret = {"year": budget.year, "month": month_num_to_name(budget.month), "items": {}}
    for budget_item in budget_items:
        if budget_item.category not in budget_ret['items']:
            budget_ret['items'][budget_item.category] = {}

        i = {
            "max": budget_item.max,
            "type": budget_item.type
        }
        budget_ret['items'][budget_item.category][budget_item.sub_category] = i
    return json.dumps(budget_ret)

