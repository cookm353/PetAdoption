from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    name = StringField('Name:', validators=[InputRequired(message='Please enter a name')])
    species = SelectField('Species:', validators=[InputRequired()])
    photo_url = StringField('Photo URL:', validators=[Optional(), URL()])
    age = IntegerField('Age:', validators=[Optional(), NumberRange(min=0, max=30,
                                                                  message='Age must be between %(min)s and %(max)s')])
    notes = StringField('Notes:', validators=[Optional()])
    available = BooleanField('Available?', validators=[Optional()])
    
class EditPetForm(FlaskForm):
    photo_url = StringField('Photo URL:', validators=[Optional(), URL()])
    notes = StringField('Notes:', validators=[Optional()])
    available = BooleanField('Available?', validators=[Optional()])