from django.shortcuts import render, redirect
from .models import User_data, Links
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
    user_data = User_data.objects.all()
    user_links = Links.objects.all()
    data = {
        'user_data': user_data,
        'user_links': user_links,
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
