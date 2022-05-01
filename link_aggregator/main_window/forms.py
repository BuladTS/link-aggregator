from .models import Users, Links
from django.forms import ModelForm, TextInput, PasswordInput, Textarea
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    fields = ['username', 'password1']

    widgets = {
        "Имя пользователя": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'username'
        }),
        "password1": PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password1'
        })
    }


class UsersRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        widgets = {
            "Имя пользователя": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'username'
            }),
            "password1": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password1'
            }),
            "password2": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'password2'
            })
        }


class LinksForm(ModelForm):
    class Meta:
        model = Links
        fields = ['link', 'description', 'tags']

        widgets = {
            "link": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Link'
            }),
            "description": Textarea(attrs={
                'class': 'description form-control',
                'placeholder': 'Description'
            }),
            "tags": TextInput(attrs={
                'class': 'tags form-control',
                'placeholder': ' Tags'
            }),
        }
