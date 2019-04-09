from django.urls import path, include
import shoppingapp.views as shoppingapp


app_name = 'shoppingapp'
urlpatterns = [
    path('<group_pk>', shoppingapp.view_group_purchases, name='shoppinglist'),
]