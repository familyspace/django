from django.db import models
from authapp.models import User
from groupapp.models import Group


# Create your models here.
class Task(models.Model):
    title = models.CharField(verbose_name='Формулировка задачи',
                             max_length=255)
    group = models.ForeignKey(Group,
                              verbose_name='Группа',
                              on_delete='CASCADE',
                              related_name='tasks')
    user = models.ManyToManyField(User,
                                  verbose_name='Пользователи в задаче',
                                  related_name='taskusers')
    done = models.BooleanField(default=False,
                               verbose_name='Задача выполнена')