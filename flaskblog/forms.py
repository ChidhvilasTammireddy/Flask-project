from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2,max=20)])

    email= StringField('Email', validators=[DataRequired(), Email()])

    password= PasswordField('Password', validators=[DataRequired()])

    confirm_password= PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit= SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username =username.data).first()
        if user:
            raise ValidationError('Another foodblogger got your name!. Please choose a different one!!')
    
    def validate_email(self,email):
        email = User.query.filter_by(email = email.data).first()
        if email:
            raise ValidationError('Another Foodblogger has a similar email-id, Please change!')

class LoginForm(FlaskForm):
    
    email= StringField('Email', validators=[DataRequired(), Email()])

    password= PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('Remember Me')

    submit= SubmitField('Login')






