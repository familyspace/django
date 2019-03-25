# Generated by Django 2.1.5 on 2019-03-25 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groupapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Краткое описание события')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание события')),
                ('location', models.CharField(max_length=255, verbose_name='Место проведения')),
                ('date', models.DateTimeField(verbose_name='Дата и время проведения')),
                ('group', models.ForeignKey(on_delete='CASCADE', related_name='events', to='groupapp.Group', verbose_name='Группа')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
