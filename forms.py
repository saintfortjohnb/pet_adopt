from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField, SelectField, validators
from wtforms.validators import DataRequired, URL, Optional

class AddPetForm(FlaskForm):
    """Form for adding a new pet."""

    name = StringField('Pet Name', validators=[DataRequired()])
    species = SelectField('Species', choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[DataRequired()])
    photo_url = StringField('Photo URL', validators=[URL(), Optional()])
    age = IntegerField('Age', validators=[Optional(), validators.NumberRange(min=0, max=30)])
    notes = StringField('Notes', validators=[Optional()])
    submit = SubmitField('Add Pet')

class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField('Photo URL', validators=[URL(), Optional()])
    notes = StringField('Notes', validators=[Optional()])
    available = BooleanField('Available')
    submit = SubmitField('Edit Pet')
