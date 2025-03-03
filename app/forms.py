from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

# class ContactForm(FlaskForm):
#     name = StringField("Name", validators=[DataRequired(), Length(min=2, max=50)])
#     email = StringField("Email", validators=[DataRequired(), Email()])
#     subject = StringField("Subject", validators=[DataRequired(), Length(max=100)])
#     message = TextAreaField("Message", validators=[DataRequired(), Length(min=10, max=500)])
#     submit = SubmitField("Send")

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()], render_kw={"placeholder": "Please enter your full name"})
    email = StringField("E-mail", validators=[DataRequired(), Email()], render_kw={"placeholder": "Please enter your e-mail address"})
    subject = StringField("Subject", validators=[DataRequired()], render_kw={"placeholder": "Please enter the subject for your message"})
    message = TextAreaField("Message", validators=[DataRequired()], render_kw={"placeholder": "Please enter the message you would like to send"})
    submit = SubmitField("Send")