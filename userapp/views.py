from django.contrib.auth.decorators import login_required
from django.contrib.messages import error
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from authapp.models import User
from userapp.models import UserContactList
from .forms import GroupCreationForm
from groupapp.models import Group, GroupUser, Category


# Create your views here.

@login_required
def creategroup_page(request):
    if request.method == 'POST':
        form = GroupCreationForm(request.POST)

        if form.is_valid():
            response = form.save(commit=True)
            response.add_user(request.user)
            response.save()
            return HttpResponseRedirect(reverse('userapp:usergroups'))
    else:
        form = GroupCreationForm()

    return render(request, 'userapp/creategroups.html', {'group_form': form})

@transaction.atomic
@login_required
def editgroup(request, group_pk):

    friendlyuser = GroupUser.objects.filter(group=group_pk, user=request.user.pk, role='ADM')
    if not friendlyuser:
        return HttpResponseForbidden()

    group = get_object_or_404(Group, pk=group_pk)
    form = GroupCreationForm(request.POST, instance=group)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('chatapp:chatpage', args=[group_pk]))
    else:
        form = GroupCreationForm(instance=group)

    content = {
        'group_form': form,
        'group_pk': group_pk,
    }

    return render(request, 'userapp/editgroup.html', content)

@login_required
def removegroup(request, group_pk):
    '''
    Удаление группы
    '''
    friendlyuser = GroupUser.objects.filter(group=group_pk, user=request.user.pk, role='ADM')
    if not friendlyuser:
        return HttpResponseForbidden()

    group = get_object_or_404(Group, pk=group_pk)
    group.delete()

    return HttpResponseRedirect(reverse('userapp:usergroups'))

@login_required
def usersearch(request):
        search = request.GET.get("query")
        relations = UserContactList.objects.filter(user=request.user.pk)
        friends = []
        for i in relations:
            friends.append(i.contact_user)

        if search:
            match = User.objects.filter(Q(email__icontains=search))
            excl = match.exclude(pk=request.user.pk)
            for i in excl:
                for j in friends:
                    if i in friends:
                        excl = excl.exclude(pk=i.pk)
            if excl:
                return render(request, 'userapp/usersearch.html', {'search': excl})
            else:
                error(request, 'no results')

        return render(request, 'userapp/usersearch.html')

@login_required
def groupsearch(request):
    categories = Category.objects.all()
    search = request.GET.get("query")
    category = request.GET.get("category")
    if search:
        test = get_object_or_404(Category, name=category)
        match = Group.objects.filter(Q(title__icontains=search, category=test.pk))
        if match:
            return render(request, 'userapp/groupsearch.html', {'search': match, 'categories': categories})
        else:
            error(request, 'no results')

    content = {
        'categories': categories
    }

    return render(request, 'userapp/groupsearch.html', content)

@login_required
def adduser(request, group_pk):
    my_group = get_object_or_404(Group, pk=group_pk)
    my_group.add_user(request.user)
    return HttpResponseRedirect(reverse('userapp:usergroups'))

@login_required
def removeuser(request, group_pk):
    group_user = get_object_or_404(GroupUser, user=request.user, group=group_pk)
    group_user.delete()
    return HttpResponseRedirect(reverse('userapp:usergroups'))

@login_required
def view_user_contacts(request):
    '''
    Просмотр списка друзей пользователя по его pk
    '''

    relations = UserContactList.objects.filter(user=request.user.pk)
    contacts = map(lambda item: item.contact_user, relations)
    content = {
        'contacts': contacts,
    }

    return render(request, 'userapp/usercontacts.html', content)

@login_required
def addcontact(request, friend_pk):
    me = get_object_or_404(User, pk=request.user.pk)
    friend = get_object_or_404(User, pk=friend_pk)
    UserContactList.objects.create(user=me, contact_user=friend)
    return HttpResponseRedirect(reverse('userapp:usersearch'))

@login_required
def removecontact(request, friend_pk):
    group_user = get_object_or_404(UserContactList, contact_user=friend_pk)
    group_user.delete()
    return HttpResponseRedirect(reverse('userapp:usercontacts'))

