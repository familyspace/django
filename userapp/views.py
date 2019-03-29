from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import GroupCreationForm
from groupapp.models import Group

# Create your views here.

@login_required
def userpage(request):
    groups = Group.objects.filter(user=request.user)
    check = 'контролер считывается'

    content = {
        'grouplist': groups,
        'test': check
    }
    return render(request, 'userapp/userpage.html', content)

@login_required
def creategroup_page(request):
    if request.method == 'POST':
        form = GroupCreationForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.user = request.user
            response.save()
            return HttpResponseRedirect(reverse('userapp:creategroups'))
    else:
        form = GroupCreationForm()

    return render(request, 'userapp/creategroups.html', {'group_form': form})
