from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.models import User
from .forms import GroupCreationForm
from groupapp.models import Group, GroupUser

# Create your views here.

@login_required
def creategroup_page(request, user_pk):
    if request.method == 'POST':
        form = GroupCreationForm(request.POST)

        if form.is_valid():
            response = form.save(commit=True)
            usergroupform = GroupUser()
            usergroupform.user = request.user
            usergroupform.group = response
            # usergroupform.role = 'Администратор'
            usergroupform.save()
            # response.user.add(request.user)
            response.save()
            return HttpResponseRedirect(reverse('userapp:userpage'))
    else:
        form = GroupCreationForm()

    return render(request, 'userapp/creategroups.html', {'group_form': form})

