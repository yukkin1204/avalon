from flask_sqlalchemy import SQLAlchemy
from . import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    date = db.Column(db.Date, nullable=False)
    progress = db.Column(db.Integer, nullable=False)

    @staticmethod
    def list():
        games = db.session.query(Game) \
                            .order_by(Game.id) \
                            .all()
        return games


