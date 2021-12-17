from flask import flash
from flask_wtf import FlaskForm #pip install flask-wtf
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, RadioField #StringField is a inputbox & SubmitFueld is a submit button
from wtforms.validators import DataRequired, EqualTo, Length, Email #to validate data inputs, and check password
from wtforms.widgets import TextArea
from flask_ckeditor import CKEditorField 

def pw_length_check(form, field):
        if len(field.data) < 8:
            flash("Password Must Be Greater Than Eight Characters.")

    # Create Signup
class SignupForm(FlaskForm):
    member_email = StringField("Email", validators=[DataRequired(), Email()])
    name = StringField("Name", validators=[DataRequired()])
    password_hash = PasswordField("Password", validators=[DataRequired(), EqualTo('password_hash2', message="Passwords Must Match"), Length(min=8), pw_length_check])
    password_hash2 = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=8), pw_length_check])
    submit = SubmitField("Submit")
    
class SigninForm(FlaskForm):
    member_email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8), pw_length_check])
    submit = SubmitField("Submit")
    
class BookCommentForm(FlaskForm):
    title = StringField("", validators=[DataRequired()])
    score = RadioField("Score", choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    content = CKEditorField('', validators=[DataRequired()])
    submit = SubmitField("Submit")

class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField("Submit")
    
    
    
    
    
    