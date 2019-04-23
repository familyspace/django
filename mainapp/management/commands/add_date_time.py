from django.core.management.base import BaseCommand
from eventapp.models import Hour, Minute, Day, Month, Year

class Command(BaseCommand):

    def handle(self, *args, **options):
        Hour.objects.all().delete()
        Minute.objects.all().delete()
        Day.objects.all().delete()
        Month.objects.all().delete()
        Year.objects.all().delete()
        print('Все данные удалены')

        i = 0
        while i < 10:
            Hour.objects.create(name='0' + str(i))
            i = i + 1
        while i < 24:
            Hour.objects.create(name=str(i))
            i = i + 1
        print('Часы добавлены')

        Minute.objects.create(name='00')
        Minute.objects.create(name='15')
        Minute.objects.create(name='30')
        Minute.objects.create(name='45')

        print('Минуты добавлены')

        i = 0
        while i < 9:
            i = i + 1
            Day.objects.create(name='0' + str(i))

        while i < 31:
            i = i + 1
            Day.objects.create(name=str(i))

        print('Дни добавлены')

        i = 0
        while i < 9:
            i = i + 1
            Month.objects.create(name='0' + str(i))

        while i < 12:
            i = i + 1
            Month.objects.create(name=str(i))

        print('Месяцы добавлены')

        Year.objects.create(name='2019')
        Year.objects.create(name='2020')
        Year.objects.create(name='2021')

