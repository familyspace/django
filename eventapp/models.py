from django.db import models
from groupapp.models import Group
from authapp.models import User
from enum import Enum


# Create your models here.

class StatusChoice(Enum):
    '''
    Задание списка перечесления для поля таблицы через класс
    '''
    ACT = 'Активно'
    INA = 'Неактивно'

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
    status = models.CharField(verbose_name='Статус',
                            max_length=3,
                            choices=[(item.name, item.value) for item in StatusChoice],
                                   blank=True,
                                   null=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        str_date = ' ' + str(self.date)
        return self.title + str_date

    def add_participant(self, user, role):
        EventUser.objects.create(user=user, event=self, role=role)
        comment = 'Участник добавлен'
        return comment

class Hour(models.Model):
    name = models.CharField(max_length=2)

    def __str__(self):
        if len(self.name) == 1:
            vis_name = '0' + self.name
        else:
            vis_name = self.name
        return vis_name

class Minute(models.Model):
    name = models.CharField(max_length=2)

    def __str__(self):
        if len(self.name) == 1:
            vis_name = '0' + self.name
        else:
            vis_name = self.name
        return ':' + vis_name

class Day(models.Model):
    name = models.CharField(max_length=2)

    def __str__(self):
        if len(self.name) == 1:
            vis_name = '0' + self.name
        else:
            vis_name = self.name
        return vis_name

class Month(models.Model):
    name = models.CharField(max_length=2)

    def __str__(self):
        if len(self.name) == 1:
            vis_name = '0' + self.name
        else:
            vis_name = self.name
        return vis_name

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
                            choices=[(item.name, item.value) for item in RoleChoice])
    event = models.ForeignKey(Event, related_name='eventusers', on_delete='CASCADE')

    def __str__(self):
        return self.event.title + ' ' + self.user.username


