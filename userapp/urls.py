from django.urls import path, include
import userapp.views as userapp
import groupapp.views as groupapp


app_name = 'userapps'
urlpatterns = [
    path('', groupapp.view_all_groups, name='userpage'),
    path('usergroups/<user_pk>', groupapp.view_user_groups, name='usergroups'),
    path('creategroup/<user_pk>', userapp.creategroup_page, name='creategroups'),
    path('usersearch/', userapp.usersearch, name='usersearch'),
    path('groupsearch/', userapp.groupsearch, name='groupsearch'),
]
