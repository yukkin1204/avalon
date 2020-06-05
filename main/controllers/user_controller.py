import flask
from flask import render_template, request, redirect
from main import app
from main.models.user import User
from main.forms import LoginForm, SignupForm

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
    form = SignupForm()
    return render_template('signup.html', title='Signup', form=form)

@app.route('/signup', methods=['POST'])
def signup():
    form = SignupForm
    user = User()
    user.id = request.form['id']
    user.password = request.form['password']
    if User.save(user):
        return redirect('/')
    else:
        return show_signup()

@app.route('/login', methods=['GET'])
def show_login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

@app.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    user = User.query.filter_by(id=form.id.data).first()
    if user is None or not user.password == form.password.data:
        return redirect('/login')
    return redirect('/users')

