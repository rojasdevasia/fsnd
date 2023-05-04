from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import setup_db, Movie, Actor, Cast

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  # CORS(app, resources={r"/api/*": {"origins": "*"}})

  return app

APP1 = create_app()
db = setup_db(APP1)

@APP1.route('/')
def index():
  return { 'HelloWorld' : 'Welcome to FSND capstone project...' }

