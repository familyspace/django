from django.conf import settings
from django.db import models
from enum import Enum
from authapp.models import FamilyUser


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(verbose_name='Название категории',
                                     max_length=100,
                                     blank=False,
                                     null=False)

    def __str__(self):
        return self.category_name


class Group(models.Model):
    user = models.ForeignKey(FamilyUser,
                             on_delete=models.CASCADE,
                             related_name="usergroups"),
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
        return self.title


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
    User = models.ForeignKey(FamilyUser, verbose_name='Пользователь',on_delete='CASCADE')
    role = models.CharField(verbose_name='Роль',
                            max_length=3,
                            choices=[(item, item.value) for item in RoleChoice],
                            default=RoleChoice.ADM)
    group = models.ForeignKey(Group, related_name='groupusers', on_delete='CASCADE')
