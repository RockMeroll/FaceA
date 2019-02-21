from django import forms
from .validators import *


class UserLoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=20, validators=[])
    password = forms.CharField(label='password', widget=forms.PasswordInput())


class UserRegisterForm(UserLoginForm):
    first_name = forms.CharField(label='first_name', max_length=30)
    last_name = forms.CharField(label='last_name', max_length=150)
    email = forms.EmailField(label='email')
    phone = forms.CharField(label='phone', max_length=11, validators=[])
    mac = forms.CharField(label='mac', max_length=20, validators=[])
    is_teacher = forms.BooleanField(label='is_teacher', required=False, initial=False)
