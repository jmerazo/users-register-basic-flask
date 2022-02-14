from src import app
from flask import render_template, redirect, request, flash
from src.controllers.users import UserController
from src.events.logs import Logs
from src.forms.forms import UserForm

userController = UserController()
logs = Logs()

@app.route('/', methods=['POST'])
def createUser():
    
    userForm = UserForm()
    
    context = {
        'userForm' : userForm
    }
    
    if request.method == 'POST' and userForm.validate():
        names = request.form['names']
        email = request.form['email']
        city = request.form['city']
        
        logs.saveLogs(names,email,city)

        userController.createUser(names,email,city)
        return render_template('index.html', userForm = userForm)
    else:
        flash('Input data validate')
        return render_template('index.html', userForm = userForm)
        

@app.route('/list_users', methods=['GET'])
def listUsers():
    users = userController.listUser()
    return render_template('list_users.html', users = users)