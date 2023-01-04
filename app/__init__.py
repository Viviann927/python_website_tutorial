import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# from config import Config

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
bootstrap = Bootstrap(app)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

bcrypt = Bcrypt(app)

# SECRET_KEY
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'A-VERY-LONG-SECRET-KEY'
# RECAPTCHA_PUBLIC_KEY
app.config['RECAPTCHA_PUBLIC_KEY'] = os.environ.get('RECAPTCHA_PUBLIC_KEY') or '6LdfdMwjAAAAAFxwBIQN-CiOPmLLrNqnBtMzaJVR'
# RECAPTCHA_PRIVATE_KEY config set
app.config['RECAPTCHA_PRIVATE_KEY'] = os.environ.get('RECAPTCHA_PRIVATE_KEY') or '6LdfdMwjAAAAACM77lIwxTF0wJrUTlAirOfZ_eUr'

from app.routes import *