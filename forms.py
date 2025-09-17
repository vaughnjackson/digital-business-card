from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    """Contact form with validation"""
    name = StringField(
        'Name', 
        validators=[
            DataRequired(message="Please enter your name."),
            Length(min=2, max=50, message="Name must be between 2 and 50 characters.")
        ]
    )
    
    email = StringField(
        'Email', 
        validators=[
            DataRequired(message="Please enter your email address."),
            Email(message="Please enter a valid email address.")
        ]
    )
    
    message = TextAreaField(
        'Message', 
        validators=[
            DataRequired(message="Please enter a message."),
            Length(min=10, max=500, message="Message must be between 10 and 500 characters.")
        ]
    )
    
    submit = SubmitField('Send Message')
