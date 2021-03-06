from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import uuid


#adding flask security for passwords
from werkzeug.security import generate_password_hash, check_password_hash

#creates hex token for our API access
import secrets 

#imports login manager from flask_login package
from flask_login import LoginManager, UserMixin


db = SQLAlchemy()

login_manager=LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
    

#new_user= User('honggao@gmail.com','1234')

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key= True)
    email = db.Column(db.String(150), nullable= False, unique=True) 
    password =db.Column(db.String, nullable=False) #people need a password to sign up (nullable)
    token= db.Column(db.String, unique= True, default ='')
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self,email, password, token='', id=''):
        self.id=self.set_id()
        self.email=email
        self.password= self.set_password(password) 
        self.token = self.set_token(24)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash= generate_password_hash(password)
        return self.pw_hash

    def set_token(self,length):
        return secrets.token_hex(length)



    


