from django.urls import path
from mainapp.views import IndexView

app_name = 'mainapp'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
