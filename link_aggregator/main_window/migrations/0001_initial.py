# Generated by Django 4.0.2 on 2022-05-17 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=1000, verbose_name='Ссылка')),
                ('description', models.TextField(verbose_name='Описание')),
                ('tags', models.CharField(max_length=250, verbose_name='Теги')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
                ('id_crated_user', models.CharField(default=5, max_length=1000, verbose_name='ID создавшего пользователя')),
            ],
            options={
                'verbose_name': 'Ссылку',
                'verbose_name_plural': 'Ссылки',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='User_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('file_type', models.CharField(max_length=50, verbose_name='Тип')),
                ('data', models.DateTimeField(verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'Файл пользователя',
                'verbose_name_plural': 'Файлы пользователей',
            },
        ),
        migrations.CreateModel(
            name='UserFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/', verbose_name='Файл')),
                ('description', models.TextField(verbose_name='Описание')),
                ('tags', models.CharField(max_length=250, verbose_name='Теги')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('id_crated_user', models.CharField(default=5, max_length=1000, verbose_name='ID создавшего пользователя')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20, verbose_name='username')),
                ('password', models.CharField(max_length=20, verbose_name='Пароль')),
                ('repeat_password', models.CharField(max_length=20, verbose_name='Повтор пароля')),
            ],
            options={
                'verbose_name': 'Логин и пароль',
                'verbose_name_plural': 'Логины и пароли',
            },
        ),
    ]
