from django.urls import path, include
import eventapp.views as eventapp


app_name = 'eventapp'

urlpatterns = [
    path('show_events/<group_pk>', eventapp.show_events, name='show_events'),
    path('create_event/<group_pk>', eventapp.create_event, name='create_event'),
    path('read_event/<event_pk>', eventapp.read_event, name='read_event'),
    path('leave_event/<event_pk>', eventapp.leave_event, name='leave_event'),
    path('join_event/<event_pk>', eventapp.join_event, name='join_event'),
]
