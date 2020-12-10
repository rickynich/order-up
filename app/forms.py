from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.fields import PasswordField, StringField, SubmitField


class LoginForm(FlaskForm):
  employee_number = StringField('Employee number', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Login')
