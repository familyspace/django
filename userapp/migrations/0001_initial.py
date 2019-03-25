# Generated by Django 2.1.5 on 2019-03-25 10:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserContactList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_user', models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL, verbose_name='Контакт пользователя')),
                ('user', models.ForeignKey(on_delete='CASCADE', related_name='contacts', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]