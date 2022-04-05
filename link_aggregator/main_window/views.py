from django.shortcuts import render, redirect
from .models import UserData
from .forms import UsersForm, LinksForm


def index(request):
    errors = ''
    if request.method == 'POST':
        form = LinksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            errors = 'Неверно'

    form = LinksForm
    user_data = UserData.objects.all()
    data = {
        'Угар': 'Необьятный океан yyyyyy',
        'Топ': ['Bleach', 'Seven deadly sing', 'Kaguya sama'],
        'Kirito': {
            'car': 'Asuna',
            'hobby': 'kill mobs',
            'age': 18
        },
        'user_data': user_data,
        'form': form,
        'errors': errors
    }

    return render(request, 'main_window/index.html', data)


def registrations(request):
    errors = ''
    if request.method == 'GET':
        form = UsersForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('authorization')
        else:
            errors = 'Заполните поля'

    form = UsersForm()
    data = {
        'form': form,
        'errors': errors
    }
    return render(request, 'main_window/registrations.html', data)


def authorization(request):
    return render(request, 'main_window/authorization.html')
