from django.urls import path, include

from api.apiuserapp.views import UserProfileViewSet, GetUserGroups
#
# urlpatterns = [
#     path('profile/', UserProfileViewSet, name='apiprofile'),
# ]


from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'user_profile_api', UserProfileViewSet, basename='profile')

urlpatterns = [path('user_groups_api/', GetUserGroups.as_view(), name='getusergroups'),
               ] + router.urls
