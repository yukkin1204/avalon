from main import db
from flask_sqlalchemy import SQLAlchemy

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, not_null=True)
    date = db.Column(db.Date, not_null=True)
    progress = db.Column(db.Integer, not_null=True)



