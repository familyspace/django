from django.db import models
from authapp.models import FamilyUser
from groupapp.models import Group


# Create your models here.


class ShopingItem(models.Model):
    title = models.CharField(verbose_name='Название товара',
                             max_length=255)
    group = models.ForeignKey(Group,
                              verbose_name='Группа',
                              on_delete='CASCADE',
                              related_name='shopingitems')
    user = models.ManyToManyField(FamilyUser, verbose_name='Пользователи в закупке')
    done = models.BooleanField(default=False,
                               verbose_name='Покупка совершена')
    price = models.DecimalField(verbose_name='Цена покупки',
                                default=0,
                                max_digits=5,
                                decimal_places=2)
    comment = models.CharField(max_length=255,
                               verbose_name='Коментарий к покупке',
                               blank=True)
