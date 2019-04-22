from django.db import models
from authapp.models import User
from groupapp.models import Group


# Create your models here.
class Chat(models.Model):
    '''
    Чат пользователей
    '''
    group = models.ForeignKey(Group,
                              verbose_name='Группа',
                              on_delete='CASCADE',
                              related_name='chat')
    user = models.ForeignKey(User,
                             verbose_name='Пользователь написавший сообщение',
                             on_delete='CASCADE')
    date_modify = models.DateTimeField(verbose_name='Дата и время изменения записи',
                                       auto_now=True)
    date_create = models.DateTimeField(verbose_name='Дата и время создания записи',
                                       auto_now_add=True)
    text = models.CharField(max_length=500,
                            verbose_name='Текст сообщения')


