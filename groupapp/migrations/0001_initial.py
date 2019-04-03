# Generated by Django 2.1.5 on 2019-03-30 17:37

from django.conf import settings
from django.db import migrations, models
import groupapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, verbose_name='Название категории')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название группы')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание группы')),
                ('is_public', models.BooleanField(default=True, verbose_name='Публичная группа')),
                ('category', models.ForeignKey(on_delete='PROTECT', to='groupapp.Category', verbose_name='Категория группы')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[(groupapp.models.RoleChoice('Администратор'), 'Администратор'), (groupapp.models.RoleChoice('Пользователь'), 'Пользователь')], default=groupapp.models.RoleChoice('Администратор'), max_length=3, verbose_name='Роль')),
                ('User', models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('group', models.ForeignKey(on_delete='CASCADE', related_name='groupusers', to='groupapp.Group')),
            ],
        ),
    ]