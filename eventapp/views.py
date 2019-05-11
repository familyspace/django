from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import EventForm
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
    events = my_group.events.filter(status='ACT').order_by('date')

    events_day = []
    events_day.append(events[0])

    box_one = 0
    while box_one < len(events):

        for i in events:
            box_one = box_one + 1
            box_two = 0
            for k in events_day:
                if i.date.day == k.date.day and i.date.month == k.date.month and i.date.year == k.date.year:
                    box_two = box_two + 1
            if box_two < 1:
                events_day.append(i)

    test = set(events_day)
    print(test)

    content = {
        'events': events,
        'group_pk': group_pk,
        'events_day': events_day
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
    message = ''
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event_info = get_event_form_data(form)
            try:
                my_dt = set_date_time(event_info)
                group = get_object_or_404(Group, pk=group_pk)
                new_event = Event.objects.create(title=event_info['title'], description=event_info['description'], location=event_info['location'], group=group, date=my_dt)
                new_event.add_participant(request.user, 'INT')
                print('Новое событие создано')
                return HttpResponseRedirect(reverse('eventapp:show_events', kwargs={'group_pk': group_pk}))
                message = 'Новое событие создано'
            except ValueError:
                print('Новое событие не создано')
                message = 'Вы ввели неправильную дату, исправьте, пожалуйста!'
        else:
            print("Форма не валидна")

    else:
        current_moment = datetime.now()
        d_minutes = (current_moment.minute//15+1)*15-current_moment.minute
        delta = datetime(2019, 4, 25, 0, d_minutes, 00) - datetime(2019, 4, 25, 0, 00, 00)
        default_moment = current_moment + delta
        initial_moment = {'hour': Hour.objects.get(name=default_moment.hour).pk,
                          'minute': Minute.objects.get(name=default_moment.minute).pk,
                          'day': Day.objects.get(name=default_moment.day).pk,
                          'month': Month.objects.get(name=default_moment.month).pk,
                          'year': Year.objects.get(name=default_moment.year).pk}
        form = EventForm(initial=initial_moment)
        message = ''
        print('message: ', message)

    content = {
        'event_form': form,
        'group_pk': group_pk,
        'message': message,
    }
    return render(request, 'eventapp/create_event.html', content)

def read_event(request, event_pk, group_pk):
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
        'group_pk': group_pk,
        'event_pk': event_pk,
        'event': my_event,
        'eventusers': eventusers,
        'is_participator': is_participator,
        'is_initiator': is_initiator,
    }
    return render(request, 'eventapp/read_event.html', content)

def read_archived_event(request, event_pk, group_pk):
    my_event = get_object_or_404(Event, pk=event_pk)
    eventusers = my_event.eventusers.all()

    content = {
        'group_pk': group_pk,
        'event': my_event,
        'eventusers': eventusers,
    }
    return render(request, 'eventapp/read_archived_event.html', content)

def leave_event(request, event_pk, group_pk):
    my_event = get_object_or_404(Event, pk=event_pk)
    my_user = get_object_or_404(EventUser, user=request.user, event=my_event)
    my_user.delete()
    eventusers = my_event.eventusers.all()
    is_participator = False

    content = {
        'group_pk': group_pk,
        'event': my_event,
        'eventusers': eventusers,
        'is_participator': is_participator,
    }
    return render(request, 'eventapp/read_event.html', content)

def join_event(request, event_pk, group_pk):
    my_event = get_object_or_404(Event, pk=event_pk)
    my_event.add_participant(request.user, 'PRT')
    eventusers = my_event.eventusers.all()
    is_participator = True

    content = {
        'group_pk': group_pk,
        'event': my_event,
        'eventusers': eventusers,
        'is_participator': is_participator,
    }
    return render(request, 'eventapp/read_event.html', content)

def edit_event(request, event_pk, group_pk):
    print('Начинаем редактирование события')
    message = ''
    my_event = get_object_or_404(Event, pk=event_pk)
    # group_pk = my_event.group.pk
    if request.method == 'POST':
        form = EventForm(request.POST)

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
                return HttpResponseRedirect(reverse('eventapp:read_event', kwargs={'group_pk': group_pk, 'event_pk': event_pk}))
            except ValueError:
                message = 'Вы ввели неправильную дату, исправьте, пожалуйста!'

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
        form = EventForm(initial=initial_data)

    content = {
        'event_form': form,
        'event_pk': event_pk,
        'group_pk': group_pk,
        'message': message,
    }
    return render(request, 'eventapp/edit_event.html', content)

def copy_event(request, event_pk, group_pk):
    print('Создается новое события на основе старого')
    my_event = get_object_or_404(Event, pk=event_pk)
    group_pk = my_event.group.pk
    if request.method == 'POST':
        form = EventForm(request.POST)

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
        form = EventForm(initial=initial_data)
        message = ''

    content = {
        'event_form': form,
        'event_pk': event_pk,
        'group_pk': group_pk,
        'message': message,
    }
    return render(request, 'eventapp/copy_event.html', content)

