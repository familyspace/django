from rest_framework.routers import DefaultRouter

from api.apigroupapp.views import UsersGroups

router = DefaultRouter()

router.register(r'user', UsersGroups, basename='usersgroups')
urlpatterns = router.urls
