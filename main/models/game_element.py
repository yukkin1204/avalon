from flask_sqlalchemy import SQLAlchemy
from . import db

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), nullable=False)
    is_spy = db.Column(db.Boolean, nullable=False)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    round = db.Column(db.Integer, nullable=False)
    phase = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    is_approve = db.Column(db.Boolean, nullable=False)

class Divination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    round = db.Column(db.Integer, nullable=False)
    maiden_id = db.Column(db.Integer, nullable=False)
    target_id = db.Column(db.Integer, nullable=False)
    is_spy = db.Column(db.Boolean, nullable=False)

