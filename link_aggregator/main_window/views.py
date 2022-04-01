from django.shortcuts import render


def index(request):
    return render(request, 'main_window/index.html')


def registrations(request):
    return render(request, 'main_window/registrations.html')


def authorization(request):
    return render(request, 'main_window/authorization.html')
