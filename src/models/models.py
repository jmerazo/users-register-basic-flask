from src.connection_db.db import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String(100))
    email = db.Column(db.String(100))
    city = db.Column(db.String(100))

    def __init__(self, names, email, city):
        self.names = names
        self.email = email
        self.city = city