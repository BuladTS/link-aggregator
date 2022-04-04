from django.db import models


class User_data(models.Model):
    name = models.CharField('Название', max_length=50)
    file_type = models.CharField('Тип', max_length=50)
    data = models.DateTimeField('Дата добавления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Файл пользователя'
        verbose_name_plural = 'Файлы пользователей'


class Users(models.Model):
    login = models.CharField('Логин', max_length=20)
    password = models.CharField('Пароль', max_length=20)
    repeat_password = models.CharField('Повтор пароля', max_length=20)

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Логин и пароль'
        verbose_name_plural = 'Логины и пароли'
