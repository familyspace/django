from django.urls import path, include

from api.apiuserapp.views import UserProfileViewSet, GetUserGroups, UserSearch, ContactListViewSet
#
# urlpatterns = [
#     path('profile/', UserProfileViewSet, name='apiprofile'),
# ]


from rest_framework.routers import DefaultRouter

UserProfilerouter = DefaultRouter()
UserProfilerouter.register(r'user_api/profile', UserProfileViewSet, basename='profile')
contact_list_router = DefaultRouter()
contact_list_router.register(r'user_api/contact_list', ContactListViewSet, basename='contactlist')

urlpatterns = [path('user_api/groups/', GetUserGroups.as_view(), name='getusergroups'),
               path('user_api/search/', UserSearch.as_view(), name='usersearch'),
               ] + UserProfilerouter.urls + contact_list_router.urls
