from django.urls import path, include
import userapp.views as userapp


app_name = 'userapps'
urlpatterns = [
    path('', userapp.userpage, name='userpage'),
    path('creategroup/', userapp.creategroup_page, name='creategroups')
]
