from django.core.management.base import BaseCommand
from authapp.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        names = ['Иван', 'Петр', 'Михаил', 'Леонид', 'Александр', 'Роман', 'Дилшот', 'Олег', 'Ильяс', 'Заур']
        User.objects.all().delete()
        print('Все пользователи удалены')
        super_user = User.objects.create_superuser('Misha', 'petmik@yandex.ru', 'reimatec', first_name='Михаил', last_name='Петухов')

        i = 1
        for person in names:
            userlogin = 'test'+str(i)
            User.objects.create(username=userlogin, first_name=person, last_name=person+'ов', email=userlogin+'@yandex.ru')
            i += 1
        print('Созданы суперюзер и 10 обычных')
        test_user = User.objects.create_user('testuser', 'test@yandex.ru', 'testuser', first_name='Тест', last_name='Тестов')
        print('Создан testuser')
