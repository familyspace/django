from django.urls import path
from rest_framework.routers import DefaultRouter

from api.apigroupapp.views import UsersGroups, CategorySet, CategoryEdit, GroupEdit, GroupSearch

routerUsersGroups = DefaultRouter()
routerCategoryEdit = DefaultRouter()
routerGroupEdit = DefaultRouter()

routerUsersGroups.register(r'user_in_group_api', UsersGroups, basename='usersgroupsapi')
routerCategoryEdit.register(r'category_edit_api', CategoryEdit, basename='categoryeditapi')
routerGroupEdit.register(r'group_edit_api', GroupEdit, basename='groupeditapi')
urlpatterns = [path('category_list_api/', CategorySet.as_view(), name='categorysapi'),
               path('group_search_api/', GroupSearch.as_view(), name='groupsearchapi'),
               ] + routerUsersGroups.urls + routerCategoryEdit.urls + routerGroupEdit.urls
