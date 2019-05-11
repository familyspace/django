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

        for i in range(0, 24):
            Hour.objects.create(name=i)

        print('Часы добавлены')

        Minute.objects.create(name=0)
        Minute.objects.create(name=15)
        Minute.objects.create(name=30)
        Minute.objects.create(name=45)

        print('Минуты добавлены')

        for i in range(1, 32):
            Day.objects.create(name=i)

        print('Дни добавлены')

        for i in range(1, 13):
            Month.objects.create(name=i)

        print('Месяцы добавлены')

        Year.objects.create(name=2019)
        Year.objects.create(name=2020)
        Year.objects.create(name=2021)

