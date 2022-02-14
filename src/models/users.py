from src.models.models import Users
from src.connection_db.db import db

class UserModel():
    def createUser(self, names, email, city):
        data = Users(names, email, city)
        db.session.add(data)
        db.session.commit()

    def listUser(self):
        data = Users.query.all()
        return data