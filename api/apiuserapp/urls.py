from django.urls import path, include

from api.apiuserapp.views import UserProfileViewSet, GetUserGroups
#
# urlpatterns = [
#     path('profile/', UserProfileViewSet, name='apiprofile'),
# ]


from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'profile', UserProfileViewSet, basename='profile')

urlpatterns = [path('usergroups/', GetUserGroups.as_view(), name='getusergroups'),
               ] + router.urls
