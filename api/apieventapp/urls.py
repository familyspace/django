from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.apieventapp.views import EventViewSet, EventList

EventRouter = DefaultRouter()
EventRouter.register(r'event_api', EventViewSet, basename='eventapi')

urlpatterns = [path('event_api/<int:group_id>/list/', EventList.as_view(), name='eventlistapi'),
               ] + EventRouter.urls
