from django.urls import path
from rest_framework.routers import DefaultRouter

from api.apigroupapp.views import UsersGroups, CategorySet, CategoryEdit, GroupEdit

routerUsersGroups = DefaultRouter()
routerCategoryEdit = DefaultRouter()
routerGroupEdit = DefaultRouter()

routerUsersGroups.register(r'user', UsersGroups, basename='usersgroups')
routerCategoryEdit.register(r'categoryedit', CategoryEdit, basename='categoryedit')
routerGroupEdit.register(r'groupedit', GroupEdit, basename='groupedit')
urlpatterns = [path('category/', CategorySet.as_view(), name='categorys'),
               ] + routerUsersGroups.urls + routerCategoryEdit.urls + routerGroupEdit.urls
