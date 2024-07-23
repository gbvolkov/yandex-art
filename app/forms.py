from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class PostGeneratorForm(FlaskForm):
    tone = StringField('Стиль', validators=[DataRequired()])
    topic = StringField('Описание', validators=[DataRequired()])
    shape = StringField('Форма', validators=[DataRequired()])
    submit = SubmitField('Создать лого')

