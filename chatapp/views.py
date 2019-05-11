from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from authapp.models import User
from chatapp.forms import chatform
from groupapp.models import GroupUser, Group
from chatapp.models import Chat

# Create your views here.

def chatpage(request, group_pk):

    friendlyuser = GroupUser.objects.filter(group=group_pk, user=request.user.pk)
    if not friendlyuser:
        return HttpResponseForbidden()

    form = chatform(request.POST)

    messages = Chat.objects.filter(group=group_pk)

    if request.method == 'POST':
        if form.is_valid():
            response = form.save(commit=False)
            group = get_object_or_404(Group, pk=group_pk)
            user = get_object_or_404(User, pk=request.user.pk)
            response.group = group
            response.user = user
            response.save()
            return HttpResponseRedirect(reverse('chatapp:chatpage', args=[group_pk]))
    else:
        form = chatform()

    content = {
        'messages': messages,
        'chatform': form,
        'group_pk': group_pk
    }

    return render(request, 'chatapp/chat.html', content)
