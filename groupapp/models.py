from django.db import models
from enum import Enum
from authapp.models import User
from django.shortcuts import get_object_or_404


# Create your models here.

def get_groups_list(self):
    groups_list = Group.objects.all()
    return groups_list

def create_group(user, title, category_name):
    my_category = get_object_or_404(Category, category_name=category_name)
    my_group = Group.objects.create(title=title, category=my_category)
    my_group.add_user(user)
    print('Группа ' + title + ' создана')
    return my_group

class Category(models.Model):
    category_name = models.CharField(verbose_name='Название категории',
                                     max_length=100,
                                     blank=False,
                                     null=False)
    def __str__(self):
        return self.category_name


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
        return self.title + ' ' + self.category.category_name

    # def get_users(self):
    #     relations = GroupUser.objects.filter(group=self.pk)
    #     members = map(lambda item: item.user, relations)
    #     return members

    def get_users(self):
        relations = self.groupusers.all()
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
                            default=RoleChoice.USR)
    group = models.ForeignKey(Group, related_name='groupusers', on_delete='CASCADE')

    class Meta:
        unique_together = ('user', 'group')

    def __str__(self):
        return self.user.username + ' ' + self.group.title + ' ' + self.role
