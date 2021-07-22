from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectMultipleField
from wtforms.validators import ValidationError, DataRequired, Length


class NoValidationSelectMultipleField(SelectMultipleField):
    def pre_validate(self, form):
        pass


class PostForm(FlaskForm):
    title = TextAreaField("Give your post a title", validators=[DataRequired()])
    subtitle = TextAreaField("Give your post a subtitle")
    body = TextAreaField('Say something', validators=[DataRequired()])
    tags = NoValidationSelectMultipleField("Select tags", )
    submit = SubmitField('Submit')
