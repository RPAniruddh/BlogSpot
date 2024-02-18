from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__) 

#creating a secret key
app.config['SECRET_KEY'] = '16bb6643d81184bf9376c955ef359510'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/Projects/Blog/blogspot/site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from blogspot import routes
