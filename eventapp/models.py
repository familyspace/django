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
                              related_name='events',
                                   blank=True,
                                   null=True)
    location = models.CharField(max_length=255,
                                verbose_name='Место проведения')
    date = models.DateTimeField(verbose_name='Дата и время проведения', auto_now_add=False,
                                   blank=True,
                                   null=True)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        str_date = ' ' + str(self.date)
        return self.title + str_date

class Year(models.Model):
    name = models.CharField(max_length=4)

    def __str__(self):
        return self.name

class Month(models.Model):
    name = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class Day(models.Model):
    name = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class Hour(models.Model):
    name = models.CharField(max_length=2)

    def __str__(self):
        return self.name

class Minute(models.Model):
    name = models.CharField(max_length=3)

    def __str__(self):
        return self.name
