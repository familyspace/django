from django.contrib.auth.decorators import login_required
from django.contrib.messages import error
from django.db.models import Q
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

def usersearch(request):
        search = request.GET.get("query")
        if search:
            match = User.objects.filter(Q(username__icontains=search))
            if match:
                return render(request, 'userapp/usersearch.html', {'search': match})
            else:
                error(request, 'no results')

        return render(request, 'userapp/usersearch.html')




def groupsearch(request):
    search = request.GET.get("query")
    if search:
        match = Group.objects.filter(Q(title__icontains=search))
        if match:
            return render(request, 'userapp/groupsearch.html', {'search': match})
        else:
            error(request, 'no results')

    return render(request, 'userapp/groupsearch.html')