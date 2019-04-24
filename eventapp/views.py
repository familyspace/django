from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import EventCreationForm
from django.urls import reverse
from groupapp.models import Group
from datetime import datetime, date, time
from .models import Event, EventUser, Hour, Minute, Day, Month, Year
import pytz

# Create your views here.

def show_events(request, group_pk):
    my_group = get_object_or_404(Group, pk=group_pk)
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
                new_event = Event.objects.create(title=title, description=description, location=location, group=group, date=my_dt)
                new_event.add_participant(request.user, 'INT')
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
        current_moment = str(datetime.now().minute)
        print(current_moment)
        current_moment = str((int(current_moment))//15*15)
        print(current_moment)
        initial_moment = {'hour': Hour.objects.get(name=str(datetime.now().hour)).pk,
                          'minute': Minute.objects.get(name=current_moment).pk,
                          'day': Day.objects.get(name=str(datetime.now().day)).pk,
                          'month': Month.objects.get(name=str(datetime.now().month)).pk,
                          'year': Year.objects.get(name=str(datetime.now().year)).pk}
        form = EventCreationForm(initial=initial_moment)

    content = {
        'event_form': form,
        'group_pk': group_pk,
    }
    return render(request, 'eventapp/create_event.html', content)

def read_event(request, event_pk):
    my_event = get_object_or_404(Event, pk=event_pk)
    eventusers = my_event.eventusers.all()

    members = map(lambda item: item.user, eventusers)
    is_participator = (request.user in members)

    if is_participator:
        my_user = get_object_or_404(EventUser, user=request.user, event=my_event)
        is_initiator = (my_user.role == 'INT')

    content = {
        'event': my_event,
        'eventusers': eventusers,
        'is_participator': is_participator,
        'is_initiator': is_initiator
    }
    return render(request, 'eventapp/read_event.html', content)

def leave_event(request, event_pk):
    my_event = get_object_or_404(Event, pk=event_pk)
    my_user = get_object_or_404(EventUser, user=request.user, event=my_event)
    my_user.delete()
    eventusers = my_event.eventusers.all()
    is_participator = False

    content = {
        'event': my_event,
        'eventusers': eventusers,
        'is_participator': is_participator,
    }
    return render(request, 'eventapp/read_event.html', content)

def join_event(request, event_pk):
    my_event = get_object_or_404(Event, pk=event_pk)
    my_event.add_participant(request.user, 'PRT')
    eventusers = my_event.eventusers.all()
    is_participator = True

    content = {
        'event': my_event,
        'eventusers': eventusers,
        'is_participator': is_participator,
    }
    return render(request, 'eventapp/read_event.html', content)
