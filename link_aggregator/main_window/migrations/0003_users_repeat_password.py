# Generated by Django 4.0.2 on 2022-04-03 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_window', '0002_users_alter_user_data_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='repeat_password',
            field=models.CharField(default=0, max_length=20, verbose_name='Повтор пароля'),
            preserve_default=False,
        ),
    ]
