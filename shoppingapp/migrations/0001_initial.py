# Generated by Django 2.1.5 on 2019-04-16 16:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groupapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopingItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название товара')),
                ('done', models.BooleanField(default=False, verbose_name='Покупка совершена')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Цена покупки')),
                ('comment', models.CharField(blank=True, max_length=255, verbose_name='Коментарий к покупке')),
                ('group', models.ForeignKey(on_delete='CASCADE', related_name='shopingitems', to='groupapp.Group', verbose_name='Группа')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Пользователи в закупке')),
            ],
        ),
    ]
