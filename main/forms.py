from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    id = StringField('id', validators = [DataRequired()])
    password = PasswordField('password', validators = [DataRequired()])
    submit = SubmitField('Login')

class SignupForm(FlaskForm):
    id = StringField('id', validators = [DataRequired()])
    password = PasswordField('password', validators = [DataRequired()])
    submit = SubmitField('Signup')