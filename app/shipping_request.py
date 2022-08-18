from flask_wtf import FlaskForm
from wtforms.fields import (
    StringField, SelectField, SubmitField, BooleanField
)
from wtforms.validators import DataRequired
from map.map import map

choices = []
for city in map:
    choices.append(city)

class ShippingForm(FlaskForm):
    sender = StringField('Sender Name', validators=[DataRequired()])
    recipient = StringField('Recipient Name', validators=[DataRequired()])
    origin = SelectField('Origin', choices=choices, validate_choice=False)
    destination = SelectField('Destination', choices=choices, validate_choice=False)
    submit = SubmitField('Submit')
