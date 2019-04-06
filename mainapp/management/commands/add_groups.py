from django.core.management.base import BaseCommand
from groupapp.models import Category, Group, GroupUser
from authapp.models import User
from django.shortcuts import get_object_or_404

class Command(BaseCommand):
    def handle(self, *args, **options):
        GroupUser.objects.all().delete()
        Group.objects.all().delete()
        Category.objects.all().delete()
        Category.objects.create(name='Развлечения')
        Category.objects.create(name='Спорт')

        my_category = get_object_or_404(Category, name='Развлечения')
        Group.objects.create(title='Группа 1', category=my_category)
        Group.objects.create(title='Группа 2', category=my_category)
        my_category = get_object_or_404(Category, name='Спорт')
        Group.objects.create(title='Группа 3', category=my_category)

        my_group = get_object_or_404(Group, title='Группа 1')
        my_user = get_object_or_404(User, username='test1')
        my_group.add_user(my_user)
        my_user = get_object_or_404(User, username='test2')
        my_group.add_user(my_user)
        my_user = get_object_or_404(User, username='test3')
        my_group.add_user(my_user)
        my_user = get_object_or_404(User, username='test4')
        my_group.add_user(my_user)

        my_group = get_object_or_404(Group, title='Группа 2')
        my_user = get_object_or_404(User, username='test3')
        my_group.add_user(my_user)
        my_user = get_object_or_404(User, username='test4')
        my_group.add_user(my_user)
        my_user = get_object_or_404(User, username='test5')
        my_group.add_user(my_user)
        my_user = get_object_or_404(User, username='test6')
        my_group.add_user(my_user)
        my_user = get_object_or_404(User, username='test7')
        my_group.add_user(my_user)

        my_group = get_object_or_404(Group, title='Группа 3')
        my_user = get_object_or_404(User, username='test6')
        my_group.add_user(my_user)
        my_user = get_object_or_404(User, username='test7')
        my_group.add_user(my_user)
        my_user = get_object_or_404(User, username='test8')
        my_group.add_user(my_user)
        my_user = get_object_or_404(User, username='test9')
        my_group.add_user(my_user)
        my_user = get_object_or_404(User, username='test10')
        my_group.add_user(my_user)
