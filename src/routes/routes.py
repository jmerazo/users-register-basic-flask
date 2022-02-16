from src import app
from flask import render_template, redirect, request, url_for, flash
from src.controllers.users import UserController
from src.events.logs import Logs
from src.forms.forms import UserForm
from src.models.models import Users

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
        validateEmail = Users.query.filter(Users.email == email).first()        
        if validateEmail == None:
            userController.createUser(name,email,city)
            logs.saveLogs(name,email,city)
            return redirect(url_for('createUser'))
        else:
            flash('Email duplicate. Input email different')
            return redirect(url_for('createUser'))
                
    return render_template('index.html', **context)
    
@app.route('/list_users', methods=['GET'])
def listUsers():
    users = userController.listUser()
    return render_template('list_users.html', users = users)

@app.route('/delete/<user>', methods=['POST', 'GET'])
def deleteUser(user):
    userController.deleteUser(user)
    return redirect(url_for('listUsers'))