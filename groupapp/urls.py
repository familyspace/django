from django.urls import path, include
import groupapp.views as groupapp


app_name = 'groupapp'
urlpatterns = [

    path('<int:group_pk>/participants/', groupapp.view_one_group, name='view_one_group'), #participants
    path('<int:group_pk>/participants/invite/', groupapp.invite_user, name='invite'),
    path('<int:group_pk>/participants/invite/<friend_pk>/', groupapp.addtogroup, name='addtogroup'),
    path('<int:group_pk>/participants/<friend_pk>/', groupapp.removefromgroup, name='removefromgroup'),
    path('<int:group_pk>/participants/roleedit/<participant_pk>/', groupapp.roleedit, name='roleedit'),
    # path('<user_pk>', groupapp.view_user_groups, name='view_user_groups'),
]