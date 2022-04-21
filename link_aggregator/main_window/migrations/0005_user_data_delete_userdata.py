# Generated by Django 4.0.2 on 2022-04-19 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_window', '0004_links_rename_user_data_userdata'),
    ]

    operations = [
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
        migrations.DeleteModel(
            name='UserData',
        ),
    ]
