from django.urls import path, include

from api.apiuserapp.views import UserProfileViewSet
#
# urlpatterns = [
#     path('profile/', UserProfileViewSet, name='apiprofile'),
# ]


from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'', UserProfileViewSet, basename='profile')

urlpatterns = router.urls
