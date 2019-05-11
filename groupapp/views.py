from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from groupapp.forms import RoleEdit
from groupapp.models import Group, get_groups_list, GroupUser
from authapp.models import User
from django.shortcuts import get_object_or_404
# Create your views here.
from userapp.models import UserContactList

@login_required
def view_one_group(request, group_pk):
    '''
    Просмотр участников группы с заданным pk
    '''

    friendlyuser = GroupUser.objects.filter(group=group_pk, user=request.user.pk)
    if not friendlyuser:
        return HttpResponseForbidden()

    members = GroupUser.objects.filter(group=group_pk)
    content = {
        'members': members,
        'group_pk': group_pk
    }

    return render(request, 'groupapp/participants.html', content)

@login_required
def view_user_groups(request):
    '''
    Просмотр списка групп пользователя по его pk
    '''

    relations = GroupUser.objects.filter(user=request.user.pk)
    groups = map(lambda item: item.group, relations)

    content = {
        'groups': groups,
    }

    return render(request, 'groupapp/groupspage.html', content)

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
    GroupUser.objects.create(user=my_friend, group=my_group, role='USR')
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

@transaction.atomic
def roleedit(request, group_pk, participant_pk):
    '''
    Редактирование роли участника
    '''

    friendlyuser = GroupUser.objects.filter(group=group_pk, user=request.user.pk, role='ADM')
    if not friendlyuser:
        return HttpResponseForbidden()

    group = get_object_or_404(GroupUser, user=participant_pk, group=group_pk)
    form = RoleEdit(request.POST, instance=group)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groupapp:view_one_group', args=[group_pk]))
    else:
        form = RoleEdit(instance=group)

    content = {
        'edit_form': form,
        'group_pk': group_pk,
        'participant_pk': participant_pk,
    }

    return render(request, 'groupapp/roleedit.html', content)