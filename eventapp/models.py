from django.db import models
from groupapp.models import Group


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
                              related_name='events')
    location = models.CharField(max_length=255,
                                verbose_name='Место проведения')
    date = models.DateTimeField(verbose_name='Дата и время проведения')

    class Meta:
        ordering = ('-date',)
