from django.shortcuts import render, get_object_or_404

# Create your views here.
from groupapp.models import get_groups_list, Group


def view_all_groups(request):
    '''
    Просмотр списка всех групп
    '''
    groups = get_groups_list(request)

    content = {
        'all_groups': groups,
    }

    return render(request, 'userapp/userpage.html', content)


def view_one_group(request, group_pk):
    '''
    Просмотр участников группы с заданным pk
    '''
    try:
        mygroup = get_object_or_404(Group, pk=group_pk)
        members = mygroup.user.all()
        content = {
            'members': members
        }
    except:
        print('Такой группы не существует')
        content = {
        }

    return render(request, 'groupapp/participants.html', content)

# def view_user_groups(request, user_pk):
#     '''
#     Просмотр списка групп пользователя по его pk
#     '''
#
#     groups = Group.objects.filter(user__pk=user_pk)
#     content = {
#         'user_groups': groups,
#     }
#
#     return render(request, 'groupapp/groupspage.html', content)