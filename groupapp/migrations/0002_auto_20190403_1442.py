# Generated by Django 2.1.5 on 2019-04-03 11:42

from django.db import migrations, models
import groupapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('groupapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupuser',
            name='role',
            field=models.CharField(choices=[(groupapp.models.RoleChoice('Администратор'), 'Администратор'), (groupapp.models.RoleChoice('Пользователь'), 'Пользователь')], default=groupapp.models.RoleChoice('Администратор'), max_length=3, verbose_name='Роль'),
        ),
        migrations.AlterUniqueTogether(
            name='groupuser',
            unique_together=set(),
        ),
    ]
