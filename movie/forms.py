from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, SelectField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange, ValidationError

def streaming_selected(form, field):
   if not form.max.data and form.netflix.data and not form.hulu.data and not form.prime.data and not form.appletv.data:
      raise ValidationError('At least one streaming service must be selected')

class Movie(FlaskForm):
   max = BooleanField('Max') 
   netflix = BooleanField('Netflix')
   hulu = BooleanField('Hulu')
   prime = BooleanField('Prime')
   appletv = BooleanField('Apple TV', validators=[streaming_selected])
   min_rating = DecimalField('Min Rating', validators=[DataRequired(), NumberRange(min=0.0, max=10.0)])
   max_rating = DecimalField('Max Rating', validators=[DataRequired(), NumberRange(min=0.0, max=10.0)])
   min_year = IntegerField('Min Year', validators=[DataRequired(), NumberRange(min=1900, max=2025)])
   max_year = IntegerField('Max Year', validators=[DataRequired(), NumberRange(min=1900, max=2025)])
   genre = SelectField('Genre', choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Animation', 'Animation'),
   ('Biography', 'Biography'),('Comedy', 'Comedy'),('Crime', 'Crime'),('Documentary', 'Documentary'),('Drama', 'Drama'),
   ('Family', 'Family'),('Fantasy', 'Fantasy'),('History', 'History'),('Horror', 'Horror'),('Music', 'Music'),
   ('Musical', 'Musical'),('Mystery', 'Mystery'),('Romance', 'Romance'),('Sci-fi', 'Sci-Fi'),('Sport', 'Sport'),
   ('Thriller', 'Thriller'),('War', 'War'),('Western', 'Western')],
    validators=[DataRequired()]
)
   submit = SubmitField('Submit')