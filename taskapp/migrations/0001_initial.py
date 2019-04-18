# Generated by Django 2.1.5 on 2019-04-17 08:07

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
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Формулировка задачи')),
                ('done', models.BooleanField(default=False, verbose_name='Задача выполнена')),
                ('group', models.ForeignKey(on_delete='CASCADE', related_name='grouptasks', to='groupapp.Group', verbose_name='Группа')),
                ('user', models.ManyToManyField(related_name='taskusers', to=settings.AUTH_USER_MODEL, verbose_name='Пользователи в задаче')),
            ],
        ),
    ]
