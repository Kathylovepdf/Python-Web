from django import forms
from django.core.exceptions import ValidationError


def words_validator(content):
    if len(content) < 4:
        raise ValidationError('not enough words')


def content_validator(content):
    keywords = ["钱", "发票"]
    for keyword in keywords:
        if keyword in content:
            raise ValidationError('Do not use that words')


class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    content = forms.CharField(
        widget=forms.Textarea(),
        error_messages={
            'required': 'please write something'
        },
        validators=[words_validator, content_validator]
    )
