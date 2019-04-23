# Generated by Django 2.1.5 on 2019-04-23 05:51

from django.conf import settings
from django.db import migrations, models


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
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
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
            ],
        ),
        migrations.CreateModel(
            name='GroupUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('ADM', 'Администратор'), ('USR', 'Пользователь')], default='ADM', max_length=3, verbose_name='Роль')),
                ('group', models.ForeignKey(on_delete='CASCADE', related_name='users', to='groupapp.Group')),
                ('user', models.ForeignKey(on_delete='CASCADE', related_name='usergroups', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
