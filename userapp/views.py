from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.models import User
from .forms import GroupCreationForm
from groupapp.models import Group

# Create your views here.

@login_required
def userpage(request):
    groups = Group.objects.filter(user=request.user)

    content = {
        'grouplist': groups,
    }
    return render(request, 'groupapp/groupspage.html', content)

@login_required
def creategroup_page(request, user_pk):
    if request.method == 'POST':
        form = GroupCreationForm(request.POST)
        if form.is_valid():
            response = form.save(commit=True)
            response.user.add(request.user)
            response.save()
            return HttpResponseRedirect(reverse('userapp:userpage'))
    else:
        form = GroupCreationForm()

    return render(request, 'userapp/creategroups.html', {'group_form': form})
