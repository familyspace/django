from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from groupapp.models import Group, get_groups_list, GroupUser
from authapp.models import User
from django.shortcuts import get_object_or_404
# Create your views here.
from userapp.models import UserContactList


@login_required
def userpage(request):
    '''
    Стартовая страница с меню приложения
    '''
    # groups = get_groups_list(request)
    #
    # content = {
    #     'groups': groups,
    # }

    return render(request, 'userapp/userpage.html')

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

@login_required
def group_menu(request, group_pk):
    '''
    Просмотр функционала группы
    '''

    friendlyuser = GroupUser.objects.filter(group=group_pk, user=request.user.pk)
    if not friendlyuser:
        return HttpResponseForbidden()

    content = {
        'group_pk': group_pk
    }

    return render(request, 'groupapp/groupmenu.html', content)

@login_required
def invite_user(request, group_pk):
    '''
    Просмотр списка друзей пользователя по его pk, перед добавлением в группу
    '''

    relations = UserContactList.objects.filter(user=request.user.pk)
    contacts = map(lambda item: item.contact_user, relations)
    friendlyusers = GroupUser.objects.filter(group=group_pk)
    ingroup = []
    for i in friendlyusers:
        ingroup.append(i.user)

    content = {
        'contacts': contacts,
        'ingroup': ingroup,
        'group_pk': group_pk
    }

    return render(request, 'groupapp/contactlist.html', content)


@login_required
def addtogroup(request, group_pk, friend_pk):
    '''
    Добавление пользователя из списка друзей в группу
    '''
    my_group = get_object_or_404(Group, pk=group_pk)
    my_friend = get_object_or_404(User, pk=friend_pk)
    my_group.add_user(my_friend)
    return HttpResponseRedirect(reverse('groupapp:invite', args=[group_pk]))

@login_required
def removefromgroup(request, group_pk, friend_pk):
    '''
    Удаление пользователя из группы залогиненным пользователем
    '''
    my_friend = get_object_or_404(User, pk=friend_pk)
    group_user = get_object_or_404(GroupUser, user=my_friend, group=group_pk)
    group_user.delete()
    return HttpResponseRedirect(reverse('groupapp:view_one_group', args=[group_pk]))