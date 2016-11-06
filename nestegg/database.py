from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

db = SQLAlchemy()

class Budget(db.Model):
    __table_args__ = (UniqueConstraint('year', 'month'),)

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)

class Bucket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    amount = db.Column(db.Integer, nullable=False)

    def __init__(self, name):
        self.name = name
        self.amount = 0

class BudgetItem(db.Model):
    __table_args__ = (UniqueConstraint('category', 'sub_category', 'budget_id'),)

    id = db.Column(db.Integer, primary_key=True)

    sub_category = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    max = db.Column(db.Integer, nullable=False)

    budget_id = db.Column(db.Integer, db.ForeignKey('budget.id'), nullable=False)
    budget = db.relationship('Budget', backref=db.backref('BudgetItem', lazy='dynamic'))

class Trans(db.Model):
    __table_args__ = (UniqueConstraint('title', 'amount', 'date', 'budget_item_id'),)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    amount = db.Column(db.Float)
    date = db.Column(db.Date)

    budget_item_id = db.Column(db.Integer, db.ForeignKey('budget_item.id'), nullable=True)
    budget_item = db.relationship('BudgetItem', backref=db.backref('Trans', lazy='dynamic'))
