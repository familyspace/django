from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import EventCreationForm
from django.urls import reverse
from groupapp.models import Group
from datetime import datetime, date, time
from .models import Event
import pytz

# Create your views here.

def show_events(request, group_pk):
    my_group = get_object_or_404(Group, pk=group_pk)
    # events = Event.objects.filter(group=my_group)
    events = my_group.events.all()
    content = {
        'events': events,
        'group_pk': group_pk,
    }

    return render(request, 'eventapp/show_events.html', content)

def create_event(request, group_pk):
    if request.method == 'POST':
        form = EventCreationForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            location = form.cleaned_data['location']
            year = form.cleaned_data['year'].name
            month = form.cleaned_data['month'].name
            day = form.cleaned_data['day'].name
            hour = form.cleaned_data['hour'].name
            minute = form.cleaned_data['minute'].name
            try:
                my_dt = datetime(int(year), int(month), int(day), int(hour), int(minute), tzinfo=pytz.UTC)
                group = get_object_or_404(Group, pk=group_pk)
                Event.objects.create(title=title, description=description, location=location, group=group, date=my_dt)
                return HttpResponseRedirect(reverse('eventapp:show_events', kwargs={'group_pk': group_pk}))
            except ValueError:
                message = 'Вы ввели неправильную дату, исправьте, пожалуйста!'
                content = {
                    'event_form': form,
                    'group_pk': group_pk,
                    'message': message,
                }
                return render(request, 'eventapp/create_event.html', content)

    else:
        form = EventCreationForm()

    content = {
        'event_form': form,
        'group_pk': group_pk,
    }

    return render(request, 'eventapp/create_event.html', content)