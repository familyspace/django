# Generated by Django 2.1.5 on 2019-05-08 15:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0010_auto_20190508_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 10, 15, 36, 37, 542209, tzinfo=utc), editable=False, verbose_name='Activation key expires'),
        ),
    ]