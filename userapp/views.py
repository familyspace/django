from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from groupapp.models import Group

from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.

# @login_required(login_url='/login/')
def mainpage(request):
    return render(request, 'userapp/index.html')


def usergroups_userapp(request):
        group = Group.objects.all()

        content = {
            'groups': group,
        }

        return render(request, 'userapp/userpage.html', content)