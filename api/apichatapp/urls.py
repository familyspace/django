from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.apichatapp.views import ChatViewSet, ChatList

ChatRouter = DefaultRouter()
ChatRouter.register(r'chat_api', ChatViewSet, basename='chatapi')

urlpatterns = [path('chat_api/<int:group_id>/list/', ChatList.as_view(), name='chatlistapi'),
               ] + ChatRouter.urls
