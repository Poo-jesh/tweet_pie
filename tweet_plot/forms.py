from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class Search(FlaskForm):
    username = StringField('Twitter User Name', validators=[DataRequired(), Length(min=1)])
