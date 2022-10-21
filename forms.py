"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, Email, URL


class AddPetForm(FlaskForm):
    """Form for adding snacks."""

    name = StringField("Pet name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = SelectField(
        'Age',
        choices=[
            ('baby', 'Baby'),
            ('young', 'Young'),
            ('adult', 'Adult'),
            ('senior', 'Senior')
        ]
    )
    notes = TextAreaField('Notes', validators=[Optional()])