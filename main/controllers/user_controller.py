import flask
from flask import request
from main import app, models
from main.models.user import User

@app.route('/users/signup/', methods=['GET'])
def show_signup():
    return flask.render_template('signup.html')


@app.route('/users/signup/', methods=['POST'])
def signup():
    user = User()
    user.id = request.form['id']
    user.password = request.form['password']
    return flask.render_template('signup_result.html', user=user)

