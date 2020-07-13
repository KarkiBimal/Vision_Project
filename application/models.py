from application import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(30), unique=True, nullable=False)
    email=db.Column(db.String(60), unique=True, nullable=False)
    password=db.Column(db.String(60), nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.date_created}')"

class Transcript(db.Model):
    id= id=db.Column(db.Integer, primary_key=True)
    transcript1=db.Column(db.String(20))
    transcript2=db.Column(db.String(20))
    transcript3=db.Column(db.String(20))
    def __repr__(self):
        return f"Transcript('{self.transcript1}','{self.transcript2}','{self.transcript3}')"

class Videos(db.Model):
   id= id=db.Column(db.Integer, primary_key=True)
   title=db.Column(db.String(20))
   path=db.Column(db.String(200))
   def __repr__(self):
        return f"Transcript('{self.path}','{self.titel}')"


    


