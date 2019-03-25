from django.db import models


# Create your models here.
from groupapp.models import Group


class ShopingItem(models.Model):
    title = models.CharField(verbose_name='Название товара',
                             max_length=255)
    group = models.ForeignKey(Group,
                              verbose_name='Группа',
                              on_delete='CASCADE',
                              related_name='shopingitems')
    # user = models.ManyToManyField(User, verbose_name='Пользователи в закупке')
