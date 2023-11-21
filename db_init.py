from flask import Flask
from app import db

# Create a Flask app instance
app = Flask(__name__)

# Configure the app and the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)

# Push the application context
app.app_context().push()

# Create the database tables
db.create_all()

# Pop the application context to avoid context leakage
# app.app_context().pop()
