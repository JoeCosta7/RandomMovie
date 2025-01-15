from wtforms import Form, BooleanField, IntegerField, StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange, ValidationError

def streaming_selected(form, field):
   if not form.max.data and form.netflix.data and not form.hulu.data and not form.prime.data and not form.appletv.data:
      raise ValidationError('At least one streaming service must be selected')

class MovieForm(Form):
   max = BooleanField('Max') 
   netflix = BooleanField('Netflix')
   hulu = BooleanField('Hulu')
   prime = BooleanField('Prime')
   appletv = BooleanField('Apple TV', validators=[streaming_selected])
   rating = DecimalField('Rating', validators=[DataRequired()], render_kw={"min": 0, "max": 10, "step": .1, "type": "range"})
   min_year = IntegerField('Min Year', validators=[DataRequired(), NumberRange(min=1900, max=2020)])
   max_year = IntegerField('Max Year', validators=[DataRequired(), NumberRange(min=1900, max=2020)])
   genre = StringField('Genre', validators=[DataRequired()])
   submit = SubmitField('Submit')