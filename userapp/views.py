from django.contrib.auth.decorators import login_required
from django.contrib.messages import error
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from authapp.models import User
from userapp.models import UserContactList
from .forms import GroupCreationForm
from groupapp.models import Group, GroupUser

# Create your views here.

@login_required
def creategroup_page(request, user_pk):
    if request.method == 'POST':
        form = GroupCreationForm(request.POST)

        if form.is_valid():
            response = form.save(commit=True)
            response.add_user(request.user)
            response.save()
            return HttpResponseRedirect(reverse('userapp:userpage'))
    else:
        form = GroupCreationForm()

    return render(request, 'userapp/creategroups.html', {'group_form': form})

@login_required
def usersearch(request):
        search = request.GET.get("query")
        if search:
            match = User.objects.filter(Q(username__icontains=search))
            if match:
                return render(request, 'userapp/usersearch.html', {'search': match})
            else:
                error(request, 'no results')

        return render(request, 'userapp/usersearch.html')

@login_required
def groupsearch(request):
    search = request.GET.get("query")
    test = User.get_contacts(request.user)
    friends = []
    for i in test:
        friends.append(i.contact_user)

    if search:
        match = Group.objects.filter(Q(title__icontains=search))
        if match:

            return render(request, 'userapp/groupsearch.html', {'search': match, 'contacts': friends})
        else:
            error(request, 'no results')

    return render(request, 'userapp/groupsearch.html')

@login_required
def adduser(request, group_pk):
    my_group = get_object_or_404(Group, pk=group_pk)
    my_group.add_user(request.user)
    return HttpResponseRedirect(reverse('userapp:userpage'))

@login_required
def removeuser(request, group_pk):
    group_user = get_object_or_404(GroupUser, user=request.user, group=group_pk)
    group_user.delete()
    return HttpResponseRedirect(reverse('userapp:userpage'))

@login_required
def view_user_contacts(request, user_pk):
    '''
    Просмотр списка друзей пользователя по его pk
    '''

    test = User.get_contacts(request.user)
    friends = []
    for i in test:
        friends.append(i.contact_user)
    print(friends)
    content = {
        'contacts': test,
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
    return HttpResponseRedirect(reverse('userapp:usercontacts', args=[request.user.pk]))

