import flask
from flask import request
from main import app, models
from main.models.user import User

@app.route('/', methods=['GET'])
def show_top():
    return flask.render_template('index.html', title='Top')

@app.route('/signup', methods=['GET'])
def show_signup():
    return flask.render_template('signup.html', title='Signup')


@app.route('/signup', methods=['POST'])
def signup():
    user = User()
    user.id = request.form['id']
    user.password = request.form['password']
    return flask.render_template('signup_result.html', title='Signup Result', user=user)

@app.route('/login', methods=['GET'])
def show_login():
    return flask.render_template('login.html')
