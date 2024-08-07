from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    company = forms.CharField(label='Компания', max_length=256, required=True, help_text='')
    # name = forms.CharField(label='Имя', max_length=100, required=True,help_text='')
    # surname = forms.CharField(label='Фамилия', max_length=100, required=True, help_text='')
    username = forms.CharField(label='Имя и фамилия', max_length=256, required=True, help_text='')

    class Meta:
        model = User
        fields = ('company', 'username', 'password1', 'password2', )
