from django.shortcuts import render, redirect
from .models import User_data, Links, UserFiles, UserDirs
from .forms import LinksForm, UserFilesForm, DeleteForm, DirForm
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UsersRegisterForm, UserLoginForm
from django.contrib.auth import login, logout


def index(request):
    errors_link = ''
    if request.method == 'POST':
        form = LinksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            errors_link = 'Неверно'

    errors_file = ''
    if request.method == 'POST':
        form = UserFilesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
            errors_file = 'Ошибка при заполнении формы'

    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            delete_data(request, data['type'], int(data['id']))

    if request.method == 'POST':
        form = DirForm(request.POST)
        if form.is_valid():
            add_directory(request, form)

    user = request.user
    delete_form = DeleteForm
    form = LinksForm
    form_file = UserFilesForm
    form_add_dir = DirForm
    user_data = User_data.objects.all()
    user_links = Links.objects.filter(id_crated_user=user.id)
    files = UserFiles.objects.filter(id_crated_user=user.id)
    dirs = UserDirs.objects.filter(id_crated_user=user.id)
    data = {
        'user_data': user_data,
        'user_links': user_links,
        'form': form,
        'errors_file': errors_file,
        'errors_link': errors_link,
        'files': files,
        'form_file': form_file,
        'delete_form': delete_form,
        'dirs': dirs,
        'form_add_dir': form_add_dir,
    }

    return render(request, 'main_window/index.html', data)


def add_directory(request, form):
    data = form.cleaned_data
    if data['parent'] == 0:
        id_crated_data = UserDirs.objects.create(name=data['name'], parent=data['parent'],
                                                 children=[0], id_crated_user=data['id_crated_user'])
        id_crated_data = id_crated_data.pk
    else:
        parent = UserDirs.objects.get(id=data['parent'])

        id_crated_data = UserDirs.objects.create(name=data['name'], parent=data['parent'],
                                                 children=[0], id_crated_user=data['id_crated_user'])
        id_crated_data = id_crated_data.pk
        parent.children.append(id_crated_data)
        parent.save(update_fields=["children"])

    index_zero = data['dates'].index(0)

    for i in range(0, len(data['dates'])):
        if i < index_zero:
            file = UserFiles.objects.get(id=data['dates'][i])
            if file.dirs["id_dirs"] == [0] or file.dirs["id_dirs"] is None:
                file.dirs = {"id_dirs": [id_crated_data]}
                file.save(update_fields=["dirs"])
            else:
                file.dirs["id_dirs"].append(id_crated_data)
                file.save(update_fields=["dirs"])
        elif i > index_zero:
            link = Links.objects.get(id=data['dates'][i])
            if link.dirs["id_dirs"] == [0] or link.dirs["id_dirs"] is None:
                link.dirs = {"id_dirs": [id_crated_data]}
                link.save(update_fields=["dirs"])
            else:
                link.dirs["id_dirs"].append(id_crated_data)
                link.save(update_fields=["dirs"])


def delete_data(request, type_del_data, id_del_data):
    if type_del_data == 'file':
        files = UserFiles.objects.get(id=id_del_data)
        files.delete()
    else:
        user_links = Links.objects.get(id=id_del_data)
        user_links.delete()

    return render(request, 'main_window/index.html')


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
