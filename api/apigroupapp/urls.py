from django.urls import path
from rest_framework.routers import DefaultRouter

from api.apigroupapp.views import UsersGroups, CategorySet, CategoryEdit, GroupEdit, GroupSearch, UserGroupsList

routerUsersGroups = DefaultRouter()
routerCategoryEdit = DefaultRouter()
routerGroupEdit = DefaultRouter()

routerUsersGroups.register(r'group_api/users', UsersGroups, basename='groupusersapi')
routerCategoryEdit.register(r'category_api/edit', CategoryEdit, basename='categoryeditapi')
routerGroupEdit.register(r'group_api/edit', GroupEdit, basename='groupeditapi')
urlpatterns = [path('category_api/list/', CategorySet.as_view(), name='categorysapi'),
               path('group_api/search/', GroupSearch.as_view(), name='groupsearchapi'),
               path('group_api/<int:group_id>/users/', UserGroupsList.as_view(), name='groupuserslistsapi'),
               ] + routerUsersGroups.urls + routerCategoryEdit.urls + routerGroupEdit.urls
