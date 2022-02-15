from src import app
from flask import render_template, redirect, request, url_for, flash
from src.controllers.users import UserController
from src.events.logs import Logs
from src.forms.forms import UserForm

userController = UserController()

@app.route('/', methods=['GET', 'POST'])
def createUser(): 
    logs = Logs()  
    user_form = UserForm(request.form)
    context = {
        'user_form': user_form
    }    
    
    if user_form.validate_on_submit():
        name = user_form.name.data
        email = user_form.email.data
        city = user_form.city.data
        
        logs.saveLogs(name,email,city)

        userController.createUser(name,email,city)
        flash('Thanks for registering')
        redirect(url_for('createUser'))
    return render_template('index.html', **context)
    
@app.route('/list_users', methods=['GET'])
def listUsers():
    users = userController.listUser()
    return render_template('list_users.html', users = users)

@app.route('/delete/<user>', methods=['POST', 'GET'])
def deleteUser(user):
    userController.deleteUser(user)
    return redirect(url_for('listUsers'))