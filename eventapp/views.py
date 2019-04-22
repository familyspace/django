from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import EventCreationForm
from django.urls import reverse
from groupapp.models import Group
from .models import Event

# Create your views here.

def show_events(request, group_pk):
    my_group = get_object_or_404(Group, pk=group_pk)
    # events = Event.objects.filter(group=my_group)
    events = my_group.events.all()
    content = {
        'events': events,
    }

    return render(request, 'eventapp/show_events.html', content)

def create_event(request, group_pk):
    if request.method == 'POST':
        form = EventCreationForm(request.POST)

        if form.is_valid():
            response = form.save(commit=True)
            response.group = get_object_or_404(Group, pk=group_pk)
            response.save()
            print(group_pk)
            return HttpResponseRedirect(reverse('groupapp:view_one_group', kwargs={'group_pk': group_pk}))
    else:

        form = EventCreationForm()
    content = {
        'event_form': form,
        'group_pk': group_pk,
    }

    return render(request, 'eventapp/create_event.html', content)