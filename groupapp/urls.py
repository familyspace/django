from django.urls import path, include
import groupapp.views as groupapp


app_name = 'groupapp'
urlpatterns = [
    path('', groupapp.view_all_groups, name='view_all_groups'),
    path('participants/<group_pk>', groupapp.view_one_group, name='view_one_group'), #participants
    path('groupmenu/<group_pk>', groupapp.group_menu, name='groupmenu'),
    # path('<user_pk>', groupapp.view_user_groups, name='view_user_groups'),
]