from django.urls import path, include
import chatapp.views as chatapp


app_name = 'shoppingapp'
urlpatterns = [
    path('', chatapp.chatpage, name='chatpage'),
]