from main import db
from flask_sqlalchemy import SQLAlchemy
from main.models import entry

def init():
    db.create_all()

