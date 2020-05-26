from main import db
from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.Text, not_null=True)

