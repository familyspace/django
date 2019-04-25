from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import EventCreationForm, EventEditForm
from django.urls import reverse
from groupapp.models import Group
from datetime import datetime
from .models import Event, EventUser, Hour, Minute, Day, Month, Year
import pytz

# Create your views here.

def get_event_form_data(form):
    title = form.cleaned_data['title']
    description = form.cleaned_data['description']
    location = form.cleaned_data['location']
    year = form.cleaned_data['year'].name
    month = form.cleaned_data['month'].name
    day = form.cleaned_data['day'].name
    hour = form.cleaned_data['hour'].name
    minute = form.cleaned_data['minute'].name
    data_dict = {'title': title, 'description': description, 'location': location, 'year': year, 'month': month, 'day': day, 'hour': hour, 'minute': minute}
    return data_dict

def set_date_time(data_dict):
    date_time = datetime(data_dict['year'], data_dict['month'], data_dict['day'], data_dict['hour'], data_dict['minute'], tzinfo=pytz.UTC)
    return date_time

def show_events(request, group_pk):
    my_group = get_object_or_404(Group, pk=group_pk)
    all_events = my_group.events.all()
    current_moment = datetime.now()
    curr_data = datetime(current_moment.year, current_moment.month, current_moment.day, current_moment.hour, current_moment.minute, tzinfo=pytz.UTC)

    for item in all_events:
        if item.date < curr_data:
            item.status = 'INA'
            item.save()
            item_users = item.eventusers.all()
            for member in item_users:
                member.role = 'PRT'
                member.save()
    events = my_group.events.filter(status='ACT')
    content = {
        'events': events,
        'group_pk': group_pk,
    }
    return render(request, 'eventapp/show_events.html', content)

def archived_events(request, group_pk):
    my_group = get_object_or_404(Group, pk=group_pk)
    events = my_group.events.filter(status='INA')
    content = {
        'events': events,
        'group_pk': group_pk,
    }
    return render(request, 'eventapp/archived_events.html', content)

def create_event(request, group_pk):
    if request.method == 'POST':
        form = EventCreationForm(request.POST)

        if form.is_valid():
            event_info = get_event_form_data(form)
            try:
                my_dt = set_date_time(event_info)
                group = get_object_or_404(Group, pk=group_pk)
                new_event = Event.objects.create(title=event_info['title'], description=event_info['description'], location=event_info['location'], group=group, date=my_dt)
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
        current_moment = datetime.now()
        d_minutes = (current_moment.minute//15+1)*15-current_moment.minute
        delta = datetime(2019, 4, 25, 0, d_minutes, 00) - datetime(2019, 4, 25, 0, 00, 00)
        default_moment = current_moment + delta
        initial_moment = {'hour': Hour.objects.get(name=str(default_moment.hour)).pk,
                          'minute': Minute.objects.get(name=str(default_moment.minute)).pk,
                          'day': Day.objects.get(name=str(default_moment.day)).pk,
                          'month': Month.objects.get(name=str(default_moment.month)).pk,
                          'year': Year.objects.get(name=str(default_moment.year)).pk}
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
    else:
        is_initiator = False

    content = {
        'event': my_event,
        'eventusers': eventusers,
        'is_participator': is_participator,
        'is_initiator': is_initiator,
    }
    return render(request, 'eventapp/read_event.html', content)

def read_archived_event(request, event_pk):
    my_event = get_object_or_404(Event, pk=event_pk)
    eventusers = my_event.eventusers.all()

    content = {
        'event': my_event,
        'eventusers': eventusers,
    }
    return render(request, 'eventapp/read_archived_event.html', content)

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

def edit_event(request, event_pk):
    print('Начинаем редактирование события')
    my_event = get_object_or_404(Event, pk=event_pk)
    group_pk = my_event.group.pk
    if request.method == 'POST':
        form = EventEditForm(request.POST)

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
                my_event.title = title
                my_event.description = description
                my_event.location = location
                my_event.date = my_dt
                my_event.save()
                return HttpResponseRedirect(reverse('eventapp:show_events', kwargs={'group_pk': group_pk}))
            except ValueError:
                message = 'Вы ввели неправильную дату, исправьте, пожалуйста!'
                content = {
                    'event_form': form,
                    'event_pk': event_pk,
                    'message': message,
                }
                return render(request, 'eventapp/edit_event.html', content)

    else:
        event_moment = my_event.date
        initial_data = {'title': my_event.title,
                        'description': my_event.description,
                        'location': my_event.location,
                        'hour': Hour.objects.get(name=str(event_moment.hour)).pk,
                        'minute': Minute.objects.get(name=str(event_moment.minute)).pk,
                        'day': Day.objects.get(name=str(event_moment.day)).pk,
                        'month': Month.objects.get(name=str(event_moment.month)).pk,
                        'year': Year.objects.get(name=str(event_moment.year)).pk}
        form = EventEditForm(initial=initial_data)

    content = {
        'event_form': form,
        'event_pk': event_pk,
        'group_pk': group_pk,
    }
    return render(request, 'eventapp/edit_event.html', content)

def copy_event(request, event_pk):
    print('Создается новое события на основе старого')
    my_event = get_object_or_404(Event, pk=event_pk)
    group_pk = my_event.group.pk
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
                return render(request, 'eventapp/copy_event.html', content)

    else:
        current_moment = datetime.now()
        d_minutes = (current_moment.minute//15+1)*15-current_moment.minute
        delta = datetime(2019, 4, 25, 0, d_minutes, 00) - datetime(2019, 4, 25, 0, 00, 00)
        default_moment = current_moment + delta
        initial_data = {'title': my_event.title,
                        'description': my_event.description,
                        'location': my_event.location,
                        'hour': Hour.objects.get(name=str(default_moment.hour)).pk,
                        'minute': Minute.objects.get(name=str(default_moment.minute)).pk,
                        'day': Day.objects.get(name=str(default_moment.day)).pk,
                        'month': Month.objects.get(name=str(default_moment.month)).pk,
                        'year': Year.objects.get(name=str(default_moment.year)).pk}
        form = EventCreationForm(initial=initial_data)

    content = {
        'event_form': form,
        'event_pk': event_pk,
        'group_pk': group_pk,
    }
    return render(request, 'eventapp/copy_event.html', content)

