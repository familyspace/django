from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render
from groupapp.models import Group, get_groups_list, GroupUser
from authapp.models import User
from django.shortcuts import get_object_or_404
# Create your views here.

@login_required
def view_all_groups(request):
    '''
    Просмотр списка всех групп
    '''
    groups = get_groups_list(request)

    content = {
        'groups': groups,
    }

    return render(request, 'userapp/userpage.html', content)

@login_required
def view_one_group(request, group_pk):
    '''
    Просмотр участников группы с заданным pk
    '''

    friendlyuser = GroupUser.objects.filter(group=group_pk, user=request.user.pk)
    if not friendlyuser:
        return HttpResponseForbidden()

    my_group = get_object_or_404(Group, pk=group_pk)
    members = my_group.get_users()
    content = {
        'members': members,
        'group_pk': group_pk
    }

    return render(request, 'groupapp/participants.html', content)

@login_required
def view_user_groups(request, user_pk):
    '''
    Просмотр списка групп пользователя по его pk
    '''

    relations = GroupUser.objects.filter(user=user_pk)
    groups = map(lambda item: item.group, relations)

    content = {
        'groups': groups,
    }

    return render(request, 'groupapp/groupspage.html', content)


def group_menu(request, group_pk):

    friendlyuser = GroupUser.objects.filter(group=group_pk, user=request.user.pk)
    if not friendlyuser:
        return HttpResponseForbidden()

    content = {
        'group_pk': group_pk
    }

    return render(request, 'groupapp/groupmenu.html', content)