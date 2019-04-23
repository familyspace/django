from django.urls import path, include
import taskapp.views as taskapp


app_name = 'taskapp'
urlpatterns = [
    path('', taskapp.view_tasks_list, name='taskslist'),
    path('newtask/', taskapp.newtaskpage, name='newtask'),
    path('taskedit/<task_pk>/', taskapp.taskedit, name='taskedit'),
    path('taskremove/<task_pk>/', taskapp.taskremove, name='taskremove'),
]