from django.urls import path, include
import userapp.views as userapp
import groupapp.views as groupapp


app_name = 'userapps'
urlpatterns = [
    path('', groupapp.userpage, name='userpage'),
    path('usercontacts/<user_pk>', userapp.view_user_contacts, name='usercontacts'),
    path('addcontact/<friend_pk>', userapp.addcontact, name='addcontact'),
    path('removecontact/<friend_pk>', userapp.removecontact, name='removecontact'),
    path('adduser/<group_pk>', userapp.adduser, name='adduser'),
    path('removeuser/<group_pk>', userapp.removeuser, name='removeuser'),
    path('usergroups/<user_pk>', groupapp.view_user_groups, name='usergroups'),
    path('creategroup/<user_pk>', userapp.creategroup_page, name='creategroups'),
    path('editgroup/<group_pk>', userapp.editgroup, name='editgroup'),
    path('removegroup/<group_pk>', userapp.removegroup, name='removegroup'),
    path('usersearch/', userapp.usersearch, name='usersearch'),
    path('groupsearch/', userapp.groupsearch, name='groupsearch'),
]
