from django.urls import path, include
import eventapp.views as eventapp


app_name = 'eventapp'

urlpatterns = [
    path('show_events/', eventapp.show_events, name='show_events'),
    path('archived_events/', eventapp.archived_events, name='archived_events'),
    path('create_event/', eventapp.create_event, name='create_event'),
    path('read_event/<event_pk>', eventapp.read_event, name='read_event'),
    path('read_archived_event/<event_pk>', eventapp.read_archived_event, name='read_archived_event'),
    path('edit_event/<event_pk>', eventapp.edit_event, name='edit_event'),
    path('leave_event/<event_pk>', eventapp.leave_event, name='leave_event'),
    path('join_event/<event_pk>', eventapp.join_event, name='join_event'),
    path('copy_event/<event_pk>', eventapp.copy_event, name='copy_event'),
]
