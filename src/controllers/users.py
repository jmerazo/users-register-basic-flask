from src.models.users import UserModel

userModel = UserModel()

class UserController():
    def createUser(self, names, email, city):
        userModel.createUser(names, email, city)

    def listUser(self):
        return userModel.listUser()