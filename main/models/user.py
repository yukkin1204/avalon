from flask_sqlalchemy import SQLAlchemy
from . import db

class User(db.Model):
    id = db.Column(db.Text, primary_key=True)
    password = db.Column(db.Text, not_null=True)

