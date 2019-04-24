from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.apitaskapp.views import TaskList, TaskViewSet

ChatRouter = DefaultRouter()
ChatRouter.register(r'task_api', TaskViewSet, basename='taskapi')

urlpatterns = [path('task_api/<int:group_id>/list/', TaskList.as_view(), name='tasklistapi'),
               ] + ChatRouter.urls
