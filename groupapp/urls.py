from django.urls import path, include
import groupapp.views as groupapp


app_name = 'groupapp'
urlpatterns = [
    path('', groupapp.view_all_groups, name='view_all_groups'),
    path('<int:group_pk>/participants/', groupapp.view_one_group, name='view_one_group'), #participants
    path('<int:group_pk>/', groupapp.group_menu, name='groupmenu'),
    path('<int:group_pk>/participants/invite/', groupapp.invite_user, name='invite'),
    path('<int:group_pk>/participants/invite/<friend_pk>/', groupapp.addtogroup, name='addtogroup'),
    path('<int:group_pk>/participants/<friend_pk>/', groupapp.removefromgroup, name='removefromgroup'),
    # path('<user_pk>', groupapp.view_user_groups, name='view_user_groups'),
]