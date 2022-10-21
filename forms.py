"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet name", validators=[InputRequired()])
    species = SelectField(
        'Species',
        choices=[
            ('Cat', 'Cat'),
            ('Dog', 'Dog'),
            ('Porcupine', 'Porcupine')
        ]
    )
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = SelectField(
        'Age',
        choices=[
            ('Baby', 'Baby'),
            ('Young', 'Young'),
            ('Adult', 'Adult'),
            ('Senior', 'Senior')
        ]
    )
    notes = TextAreaField('Notes', validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing pets"""

    photo_url = StringField("Photo URL", validators=[InputRequired(), URL()])
    notes = TextAreaField('Notes', validators=[Optional()])
    available = BooleanField('Available')
