from Tools.scripts.ptags import tags
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
    login = models.CharField('username', max_length=20)
    password = models.CharField('Пароль', max_length=20)
    repeat_password = models.CharField('Повтор пароля', max_length=20)

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Логин и пароль'
        verbose_name_plural = 'Логины и пароли'


class Links(models.Model):
    link = models.CharField('Ссылка', max_length=1000)
    description = models.TextField('Описание')
    tags = models.CharField('Теги', max_length=250)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.tags

    class Meta:
        verbose_name = 'Ссылку'
        verbose_name_plural = 'Ссылки'
        ordering = ['-created_at']


class UserFiles(models.Model):
    file = models.FileField('Файл', upload_to='uploads/')
    description = models.TextField('Описание')
    tags = models.CharField('Теги', max_length=250)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.tags

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ['-created_at']
