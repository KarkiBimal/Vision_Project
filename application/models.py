from application import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    Username=db.Column(db.String(30), unique=True, nullable=False)
    email=db.Column(db.String(60), unique=True, nullable=False)
    password=db.Column(db.String(60), nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"User('{self.Username}','{self.email}','{self.date_created}')"

class Transcript(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    Transcript1=db.Column(db.String(20))
    Transcript2=db.Column(db.String(20))
    Transcript3=db.Column(db.String(20))
    def __repr__(self):
        return f"Transcript('{self.Transcript1}','{self.Transcript2}','{self.Transcript3}')"

class Videos(db.Model):
   id=db.Column(db.Integer, primary_key=True)
   Path=db.Column(db.String(200))
   Title=db.Column(db.String(20))
   def __repr__(self):
        return f"Videos('{self.Title}','{self.Path}')"


    


