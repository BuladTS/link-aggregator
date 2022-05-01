from django.shortcuts import render, redirect
from .models import User_data, Links
from .forms import LinksForm
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UsersRegisterForm, UserLoginForm
from django.contrib.auth import login, logout


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
    user_links = Links.objects.order_by('-created_at')
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
        form = UsersRegisterForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('authorization')
        else:
            errors = 'Заполните поля'

    form = UsersRegisterForm()
    data = {
        'form': form,
        'errors': errors
    }
    return render(request, 'main_window/registrations.html', data)


def authorization(request):
    if request.method == 'GET':
        form = UserLoginForm(data=request.GET)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')

    form = UserLoginForm()
    return render(request, 'main_window/authorization.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('authorization')
