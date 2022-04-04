from .models import Users
from django.forms import ModelForm, TextInput, PasswordInput


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['login', 'password', 'repeat_password']

        widgets = {
            "login": TextInput(attrs={
                'class': 'login',
                'placeholder': 'Login'
            }),
            "password": PasswordInput(attrs={
                'class': 'password',
                'placeholder': 'Password'
            }),
            "repeat_password": PasswordInput(attrs={
                'class': 'repeat_password',
                'placeholder': 'Repeat password'
            })
        }
