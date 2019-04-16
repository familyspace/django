from django.urls import path, include

from api.apiuserapp.views import UserProfileViewSet, GetUserGroups
#
# urlpatterns = [
#     path('profile/', UserProfileViewSet, name='apiprofile'),
# ]


from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'user_api/profile', UserProfileViewSet, basename='profile')

urlpatterns = [path('user_api/groups/', GetUserGroups.as_view(), name='getusergroups'),
               ] + router.urls
