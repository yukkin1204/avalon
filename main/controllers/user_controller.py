import flask
from flask import render_template, request, redirect
from main import app
from main.models.user import User

@app.route('/', methods=['GET'])
def show_top():
    return render_template('index.html', title='Top')

@app.route('/users', methods=['GET'])
def show_user_list():
    users = User.list()
    return render_template('users/index.html', title='User List', users=users)

@app.route('/users/<id>', methods=['POST', 'DELETE'])
def delete_user(id):
    if request.method != 'POST' \
        or request.form['_method'] == 'DELETE':
        User.delete(id)
    return redirect('/users')

@app.route('/signup', methods=['GET'])
def show_signup():
    return render_template('signup.html', title='Signup')

@app.route('/signup', methods=['POST'])
def signup():
    user = User()
    user.id = request.form['id']
    user.password = request.form['password']
    if User.save(user):
        return redirect('/')
    else:
        return show_signup()

@app.route('/login', methods=['GET'])
def show_login():
    return flask.render_template('login.html')
