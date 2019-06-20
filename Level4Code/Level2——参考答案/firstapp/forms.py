from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
from django.forms import widgets
from django.forms import fields
from django.core.exceptions import ValidationError

def word_validator(comment):
    if len(comment) < 4:
        raise ValidationError("not enough words")

def comment_validator(comment):
    keywords = [u"发票", u"钱"]
    for keyword in keywords:
        if keyword in comment:
            raise ValidationError("Your comment contains invalid words,please check it again.")

class CommentForm(forms.Form):
    # name = forms.CharField(max_length=50)
    comment = forms.CharField(
        widget=forms.Textarea(),
        error_messages = {
            "required": 'wow, such words'
            },
        validators = [word_validator, comment_validator]
        )

class UserProfileForm(forms.Form):


    name = forms.CharField(max_length=50,  label='姓名', widget=widgets.TextInput(
    attrs={'placeholder':'你的真实姓名'}
    ) )
    SEX_CHOICES = (
        ('', '性别'),
        ('boy', '男'),
        ('girl', '女'),
        )
    sex = forms.ChoiceField(choices=SEX_CHOICES, label='性别' )
    # new_psw = fields.CharField(label='密码',
    #     widget=widgets.PasswordInput(attrs={'class': 'c1'}, render_value=True)
    # )
    avatar = forms.ImageField(label='修改头像')
