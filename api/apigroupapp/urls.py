from django.urls import path
from rest_framework.routers import DefaultRouter

from api.apigroupapp.views import UsersGroups, CategorySet, CategoryEdit, GroupEdit, GroupSearch

routerUsersGroups = DefaultRouter()
routerCategoryEdit = DefaultRouter()
routerGroupEdit = DefaultRouter()

routerUsersGroups.register(r'group_api/users', UsersGroups, basename='groupusersapi')
routerCategoryEdit.register(r'category_api/edit', CategoryEdit, basename='categoryeditapi')
routerGroupEdit.register(r'group_api/edit', GroupEdit, basename='groupeditapi')
urlpatterns = [path('category_api/list/', CategorySet.as_view(), name='categorysapi'),
               path('group_api/search/', GroupSearch.as_view(), name='groupsearchapi'),
               ] + routerUsersGroups.urls + routerCategoryEdit.urls + routerGroupEdit.urls
