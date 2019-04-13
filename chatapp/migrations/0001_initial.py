# Generated by Django 2.1.5 on 2019-04-13 12:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groupapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modify', models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения записи')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания записи')),
                ('text', models.CharField(max_length=500, verbose_name='Текст сообщения')),
                ('group', models.ForeignKey(on_delete='CASCADE', related_name='chat', to='groupapp.Group', verbose_name='Группа')),
                ('user', models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь написавший сообщение')),
            ],
        ),
    ]
