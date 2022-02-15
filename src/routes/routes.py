from src import app
from flask import render_template, redirect, request, url_for
from src.controllers.users import UserController
from src.events.logs import Logs
from src.forms.forms import UserForm

userController = UserController()

@app.route('/', methods=['POST'])
def createUser(): 
    logs = Logs()  
    form = UserForm(request.form)    
    
    names = form.names.data
    email = form.email.data
    city = form.city.data
    
    logs.saveLogs(names,email,city)

    userController.createUser(names,email,city)
    return render_template('index.html', form = form)
    
@app.route('/list_users', methods=['GET'])
def listUsers():
    users = userController.listUser()
    return render_template('list_users.html', users = users)

@app.route('/delete/<user>', methods=['POST', 'GET'])
def deleteUser(user):
    userController.deleteUser(user)
    return redirect(url_for('listUsers'))