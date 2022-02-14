from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from src import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)