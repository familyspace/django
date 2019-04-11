from django.db import models
from enum import Enum

from django.shortcuts import get_object_or_404

from authapp.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name='Название категории',
                                     max_length=100,
                                     blank=False,
                                     null=False)
    def __str__(self):
        return self.name


class Group(models.Model):
    title = models.CharField(verbose_name='Название группы',
                             max_length=255,
                             blank=False,
                             null=False)
    description = models.TextField(verbose_name='Описание группы',
                                   blank=True,
                                   null=True)
    is_public = models.BooleanField(verbose_name='Публичная группа',
                                    default=True)
    category = models.ForeignKey(Category,
                                 verbose_name='Категория группы',
                                 on_delete='PROTECT')

    def __str__(self):
        return self.title + ' ' + self.category.name

    def get_users(self):
        relations = GroupUser.objects.filter(group=self.pk)
        members = map(lambda item: item.user, relations)
        return members

    def add_user(self, user):
        GroupUser.objects.create(user=user, group=self)
        comment = 'Участник добавлен'
        return comment

    def remove_user(self, user):
        group_user = get_object_or_404(GroupUser, user=user, group=self)
        print('юзер опознан')
        group_user.delete()
        print('и удален из группы')
        comment = 'Участник удален'
        return comment

def get_groups_list(self):
    groups_list = Group.objects.all()
    return groups_list


class RoleChoice(Enum):
    '''
    Задание списка перечесления для поля таблицы через класс
    '''
    ADM = 'Администратор'
    USR = 'Пользователь'

class GroupUser(models.Model):
    '''
    Таблица списка пользователей в группе
    '''
    user = models.ForeignKey(User, verbose_name='Пользователь', related_name='usergroups', on_delete='CASCADE')
    role = models.CharField(verbose_name='Роль',
                            max_length=3,
                            choices=[(item.name, item.value) for item in RoleChoice],
                            default=RoleChoice.ADM.name)
    group = models.ForeignKey(Group, related_name='users', on_delete='CASCADE')

