from flask_sqlalchemy import SQLAlchemy
from . import db

class User(db.Model):
    id = db.Column(db.String(16), primary_key=True)
    password = db.Column(db.String(16), nullable=False)

