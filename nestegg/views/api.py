import calendar
import datetime
import json

from flask import Blueprint, request, abort
from util import *
from consts import *
from database import db, Budget, Bucket, BudgetItem, Trans

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
                bucket = Bucket(attrs['bucket'])
                db.session.add(bucket)

                i.bucket = bucket

            db.session.add(i)
    db.session.commit()

    return "Good"

@api.route("/budget/add", methods=['POST'])
def budget_item_add():
    budget_item_dict = request.get_json()
    year = int(budget_item_dict['year'])
    month = month_name_to_num(budget_item_dict['month'])

    budget = Budget.query.filter_by(year=year, month=month).first_or_404()

    b = BudgetItem()
    b.budget = budget
    b.category = budget_item_dict['category']
    b.sub_category = budget_item_dict['sub_category']
    b.max = budget_item_dict['max']
    b.type = budget_item_dict['type']

    if budget_item_dict['type'] == BUDGET_TYPES['bucket']:
        bucket = Bucket.query.filter_by(name=budget_item_dict['bucket']).first_or_404()
        b.bucket = bucket

    db.session.add(b)
    db.session.commit()

    return "Good"

@api.route("/budget/get/<year>/<month>", methods=['GET'])
def budget_get(year, month):
    budget = Budget.query.filter_by(year=int(year), month=month_name_to_num(month)).first_or_404()
    budget_items = BudgetItem.query.filter_by(budget=budget).all()

    budget_ret = {"year": budget.year, "month": month_num_to_name(budget.month), "items": {}}
    for budget_item in budget_items:
        if budget_item.category not in budget_ret['items']:
            budget_ret['items'][budget_item.category] = {}

        i = {
            "id": budget_item.id,
            "max": budget_item.max,
            "type": budget_item.type
        }
        budget_ret['items'][budget_item.category][budget_item.sub_category] = i

    return json.dumps(budget_ret)

@api.route("/budgetmonths/get/all", methods=['GET'])
def budget_months_get():
    budgets = Budget.query.all()
    out =[(x.year, x.month) for x in budgets]

    return json.dumps(out)

@api.route("/subcategory/get/<year>/<month>", methods=['GET'])
def subcategory_get(year, month):
    budget = Budget.query.filter_by(year=int(year), month=month_name_to_num(month)).first_or_404()

    budget_items = BudgetItem.query.filter_by(budget=budget).all()

    out = [(x.category, x.sub_category) for x in budget_items]
    return json.dumps(out)


@api.route("/transaction/create", methods=['POST'])
def transaction_create():
    transaction_dict = request.get_json()

    t = Trans()
    t.title = transaction_dict['title']
    t.amount = float(transaction_dict['amount'])

    year, month, day = map(int, transaction_dict['date'].split("-"))
    t.date = datetime.date(year, month, day)

    t_cat, t_sub_cat = transaction_dict['budget_item']

    budget_item = BudgetItem.query.filter_by(category=t_cat, sub_category=t_sub_cat).first_or_404()
    t.budget_item = budget_item

    if budget_item.type == BUDGET_TYPES['bucket']:
        budget_item.bucket.amount += t.amount

    db.session.add(t)
    db.session.commit()

    return "Good"

@api.route("/transaction/get/all", methods=['GET'])
def transaction_get():
    trans = Trans.query.all()
    trans_out = []
    for tran in trans:
        trans_out.append({
            "id": tran.id,
            "title": tran.title,
            "amount": tran.amount,
            "date": str(tran.date),
            "budget_item": [tran.budget_item.category, tran.budget_item.sub_category]
        })

    return json.dumps(trans_out)

@api.route("/homeinfo/get", methods=['GET'])
def homeinfo_get():
    out = {"buckets": {}}

    buckets = Bucket.query.all()
    for bucket in buckets:
        out['buckets'][bucket.name] = bucket.amount

    today = datetime.date.today()
    last_day = calendar.monthrange(today.year, today.month)[1]
    transactions = Trans.query.filter(Trans.date.between(today.replace(day=1),
                                                         today.replace(day=last_day))).all()

    budget = Budget.query.filter_by(year=today.year, month=today.month).first_or_404()
    budget_items = BudgetItem.query.filter_by(budget=budget).all()

    out['total_spent'] = sum(x.amount for x in transactions)
    out['total_budgeted'] = sum(x.max for x in budget_items)


    return json.dumps(out)

@api.route("/bucket/add/<name>", methods=['POST', 'GET'])
def buckets_add(name):
    bucket = Bucket(name)
    db.session.add(bucket)
    db.session.commit()

    return "Good"

@api.route("/bucket/get/all", methods=['GET'])
def buckets_get():
    buckets = Bucket.query.all()
    out = [(x.name, x.amount) for x in buckets]
    return json.dumps(out)
