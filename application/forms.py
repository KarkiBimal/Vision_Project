from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField
from wtforms.validators import DataRequired, Length, Email , EqualTo, Length, ValidationError
from application.models import User, Transcript, Videos



class RegisterationForm(FlaskForm):
    username=StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email=StringField('Email',validators=[DataRequired(), Email()])
    password=PasswordField('Password', validators=[DataRequired(), Length(min=6, message='Select the stronger password')])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password', message='Password must match')])
    submit=SubmitField('Sign Up!')

    def validate_username(self, username):
        user=User.query.filter_by(Username=username.data).first()
        if user:
            raise ValidationError('That username is taken already')

    def validate_email(self, email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken already')


class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(), Email()])
    password=PasswordField('Password', validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login!')

class UpdateAccountForm(FlaskForm):
    username=StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email=StringField('Email',validators=[DataRequired(), Email()])
    submit=SubmitField('Update Account')

    def validate_username(self, username):
        if username.data !=current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken already')

    def validate_email(self, email):
        if email.data != current_user.email:
            user=User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken already')

class Transcriptform(FlaskForm):
    transcript1=TextField('Transcript1',validators=[Length(min=2, max=2000)])
    transcript2=TextField('Transcript2',validators=[Length(min=2, max=2000)])
    transcript3=TextField('Transcript3',validators=[Length(min=2, max=2000)])
    submit=SubmitField('Submit')

class VideosForm(FlaskForm):
    title=StringField('Title',validators=[Length(min=1,max=20)])
    submit=SubmitField('Submit')