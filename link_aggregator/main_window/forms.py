from pyexpat import model

from scipy.optimize._tstutils import description

from .models import Users, Links, UserFiles
from django.forms import ModelForm, TextInput, PasswordInput, Textarea, FileInput
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

        help_texts = {
            'username': None,
            'password1': None,
            'password2': None
        }
        widgets = {
            "Имя пользователя": TextInput(attrs={
                'class': 'login',
                'placeholder': 'username'
            }),
            "password1": PasswordInput(attrs={
                'class': 'login',
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
        fields = ['link', 'description', 'tags', 'id_crated_user']

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
            "id_crated_user": TextInput(attrs={
                'class': 'hidden',
                'id': 'id_user',
                'value': 5,
            })
        }


class UserFilesForm(ModelForm):
    class Meta:
        model = UserFiles
        fields = ['file', 'description', 'tags']

        widgets = {
            "file": FileInput(attrs={
                'class': 'form-control',
                'id': 'customFileLang',
                'type': 'file'
            }),
            "description": Textarea(attrs={
                'class': 'description form-control',
                'placeholder': 'Description'
            }),
            "tags": TextInput(attrs={
                'class': 'tags form-control',
                'placeholder': 'Tags'
            })
        }
