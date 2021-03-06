from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

UPLOAD_FOLDER='application\static\Videos'

app.config['SECRET_KEY']='ed1ff94680a9743cdb0df051afc03b5c00770af70f4d' #hex 22
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.config['MAX_CONTENT_PATH']=200 * 1024 * 1024


db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='Login'
login_manager.login_message_category='info'


from application import routes
 