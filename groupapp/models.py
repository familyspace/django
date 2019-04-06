from django.db import models
from enum import Enum
from authapp.models import User


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(verbose_name='Название категории',
                                     max_length=100,
                                     blank=False,
                                     null=False)


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
                            choices=[(item, item.value) for item in RoleChoice],
                            default=RoleChoice.ADM)
    group = models.ForeignKey(Group, related_name='groupusers', on_delete='CASCADE')
