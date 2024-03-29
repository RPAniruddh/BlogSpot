from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from blogspot.models import User, Post
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                        validators =[DataRequired(), Length(min=2, max=15)])
    email = StringField('Email',
                        validators= [DataRequired(), Email()])
    password = PasswordField('Password', 
                        validators=[DataRequired(),])
    confirm_password = PasswordField('Confirm Password',
                                     validators =[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username= username.data).first()
        if user:
            raise ValidationError('This username has already been taken, please try another one')
        
    def validate_email(self, email):
        user = User.query.filter_by(email= email.data).first()
        if user:
            raise ValidationError('This email is being used, please try another one')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators= [DataRequired(), Email()])
    password = PasswordField('Password', 
                        validators=[DataRequired(),])
    remember = BooleanField('Remember Me')   # helps users to stay loged in with the help of cookies
    submit = SubmitField('Log In')


class UpdateAccountForm(FlaskForm):
    username =StringField('Username',
                          validators=[DataRequired(), Length(min =2, max =15)])
    email =StringField('Email',
                       validators=[DataRequired(), Email()])
    picture =FileField('Update profile picture', validators=[FileAllowed(['png', 'jpg'])])
    submit =SubmitField('Update')


    def validate_username(self, username):
        if username.data != current_user.username:
            user =User.query.filter_by(username =username.data).first()
            if user:
                raise ValidationError('This username has already been taken, please try another one')
        

    def validate_email(self, email):
        if email.data != current_user.email:
            user =User.query.filter_by(email =email.data).first()
            if user:
                raise ValidationError('This email is being used, please try another one')
            

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit =SubmitField('Post')