from django.db import models
from groupapp.models import Group
from authapp.models import User
from enum import Enum


# Create your models here.

class Event(models.Model):
    title = models.CharField(verbose_name='Краткое описание события',
                             max_length=255)
    description = models.TextField(verbose_name='Описание события',
                                   blank=True,
                                   null=True)
    group = models.ForeignKey(Group,
                              verbose_name='Группа',
                              on_delete='CASCADE',
                              related_name='events',
                                   blank=True,
                                   null=True)
    location = models.CharField(max_length=255,
                                verbose_name='Место проведения')
    date = models.DateTimeField(verbose_name='Дата и время проведения',
                                   blank=True,
                                   null=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        str_date = ' ' + str(self.date)
        return self.title + str_date

    def add_participants(self, user):
        EventUser.objects.create(user=user, event=self)
        comment = 'Участник добавлен'
        return comment

class Hour(models.Model):
    name = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class Minute(models.Model):
    name = models.CharField(max_length=2)

    def __str__(self):
        return ':' + self.name

class Day(models.Model):
    name = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class Month(models.Model):
    name = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class Year(models.Model):
    name = models.CharField(max_length=4)

    def __str__(self):
        return self.name

class RoleChoice(Enum):
    '''
    Задание списка перечесления для поля таблицы через класс
    '''
    INT = 'Инициатор'
    PRT = 'Участник'

class EventUser(models.Model):
    '''
    Таблица участников в событии
    '''
    user = models.ForeignKey(User, verbose_name='Пользователь', related_name='userevents', on_delete='CASCADE')
    role = models.CharField(verbose_name='Роль',
                            max_length=3,
                            choices=[(item.name, item.value) for item in RoleChoice],
                            default=RoleChoice.PRT.name)
    event = models.ForeignKey(Event, related_name='eventusers', on_delete='CASCADE')

    def __str__(self):
        return self.event.title + ' ' + self.user.username


