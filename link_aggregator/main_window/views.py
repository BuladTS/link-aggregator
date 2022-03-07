from django.shortcuts import render


def index(request):
    return render(request, 'main_window/index.html')
