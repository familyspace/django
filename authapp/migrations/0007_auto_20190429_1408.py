# Generated by Django 2.1.5 on 2019-04-29 11:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20190429_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 1, 11, 8, 51, 529071, tzinfo=utc), editable=False, verbose_name='Activation key expires'),
        ),
    ]