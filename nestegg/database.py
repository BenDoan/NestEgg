from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)

class Bucket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    budget_id = db.Column(db.Integer, db.ForeignKey('budget.id'), nullable=False)
    budget = db.relationship('Budget', backref=db.backref('Bucket', lazy='dynamic'))

    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

class BudgetItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    sub_category = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    type = db.Column(db.String(80), nullable=False)

    max = db.Column(db.Integer, nullable=False)

    budget_id = db.Column(db.Integer, db.ForeignKey('budget.id'), nullable=False)
    budget = db.relationship('Budget', backref=db.backref('BudgetItem', lazy='dynamic'))

    bucket_id = db.Column(db.Integer, db.ForeignKey('bucket.id'), nullable=True)
    bucket = db.relationship('Bucket', backref=db.backref('BudgetItem', lazy='dynamic'))

class Trans(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    amount = db.Column(db.Float)
    date = db.Column(db.Date)

    budget_item_id = db.Column(db.Integer, db.ForeignKey('budget_item.id'), nullable=True)
    budget_item = db.relationship('BudgetItem', backref=db.backref('Trans', lazy='dynamic'))
