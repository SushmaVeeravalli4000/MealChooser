from flask_wtf import FlaskForm       
from wtforms import StringField, PasswordField, SubmitField, BooleanField    # Imports the classes and functions to work with strings and passwords
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from mealchooser.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField('Username',    #This is also the label for the HTML
        validators=[DataRequired(), Length(min=2,max=20)])    #This is to validate the input
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5)])
    remember = BooleanField('Remember Me')   # Allows login with a secure cookie
    submit = SubmitField('Login')

class RequestResetForm(FlaskForm):
    email = StringField('Email',
                         validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Resert')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
submit = SubmitField('Resert Password')

