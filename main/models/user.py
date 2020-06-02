from flask_sqlalchemy import SQLAlchemy
from . import db

class User(db.Model):
    id = db.Column(db.String(16), primary_key=True)
    password = db.Column(db.String(16), nullable=False)
    
    @staticmethod
    def save(user):
        if len(user.id) >= 3 \
            and len(user.password) >= 4:
            
            users = db.session.query(User) \
                                .filter(User.id==user.id) \
                                .all()
            
            if not users:
                db.session.add(user)
                db.session.commit()
                return True
        
        return False
    
    @staticmethod
    def list():
        users = db.session.query(User) \
                            .order_by(User.id) \
                            .all()
        return users
    
    @staticmethod
    def delete(id):
        db.session.query(User) \
                    .filter(User.id==id) \
                    .delete()
        db.session.commit()

