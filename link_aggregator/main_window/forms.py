from .models import Users, Links
from django.forms import ModelForm, TextInput, PasswordInput, Textarea


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


class LinksForm(ModelForm):
    class Meta:
        model = Links
        fields = ['link', 'description', 'tags']

        widgets = {
            "link": TextInput(attrs={
                'class': 'link',
                'placeholder': 'Link'
            }),
            "description": Textarea(attrs={
                'class': 'description',
                'placeholder': 'Description'
            }),
            "tags": TextInput(attrs={
                'class': 'tags',
                'placeholder': ' Tags'
            }),
        }
