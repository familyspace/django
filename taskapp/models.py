from django.db import models
from authapp.models import User
from groupapp.models import Group


# Create your models here.
class Task(models.Model):
    title = models.CharField(verbose_name='Формулировка задачи',
                             max_length=255)
    group = models.ForeignKey(Group,
                              verbose_name='Группа',
                              on_delete=models.CASCADE,
                              related_name='grouptasks')
    user = models.ManyToManyField(User,
                                  verbose_name='Пользователи в задаче',
                                  related_name='taskusers')
    done = models.BooleanField(default=False,
                               verbose_name='Задача выполнена')

    description = models.CharField(max_length=255,
                               verbose_name='Коментарий к покупке',
                               blank=True)

    def __str__(self):
        return self.title