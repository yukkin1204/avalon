from flask_sqlalchemy import SQLAlchemy
from . import db

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, not_null=True)
    is_spy = db.Column(db.Boolean, not_null=True)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    round = db.Column(db.Integer, not_null=True)
    phase = db.Column(db.Integer, not_null=True)
    user_id = db.Column(db.Integer, not_null=True)
    is_approve = db.Column(db.Boolean, not_null=True)

class Divination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    round = db.Column(db.Integer, not_null=True)
    maiden_id = db.Column(db.Integer, not_null=True)
    target_id = db.Column(db.Integer, not_null=True)
    is_spy = db.Column(db.Boolean, not_null=True)

