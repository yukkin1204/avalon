from main import db
from flask_sqlalchemy import SQLAlchemy

def init():
    db.create_all()

from main.models import entry

