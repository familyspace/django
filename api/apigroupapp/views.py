from django.shortcuts import render
from collections import OrderedDict

from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, \
    RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from api.apigroupapp.schemas import UsersGroupsSchema, CategorySchema, CategoryEditSchema, GroupEditSchema
from api.apigroupapp.serializers import UsersGroupsSerializer, CategorySerializer, GroupSerializer
from api.core import errorcodes
from api.core import exceptions
from api.core.renderrers import ApiJSONRenderer

from groupapp.models import GroupUser, RoleChoice, Category, Group


class UsersGroups(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin,
                  viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ApiJSONRenderer,)
    queryset = GroupUser.objects.all()
    serializer_class = UsersGroupsSerializer
    schema = UsersGroupsSchema()

    def perform_destroy(self, instance):
        # проверка наличия прав
        if not GroupUser.objects.filter(user=self.request.user,
                                        group=instance.group_id,
                                        role=RoleChoice.ADM.name):
            raise exceptions.FamilySpaceException(**errorcodes.ERR_NO_RIGHTS_FOR_ACTION)
        super().perform_destroy(instance)

    def permission_denied(self, request, message=None):
        if not request.successful_authenticator:
            raise exceptions.FamilySpaceException(**errorcodes.ERR_WRONG_TOKEN)
        super().permission_denied(request, message=None)


class CategorySet(ListAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ApiJSONRenderer,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    schema = CategorySchema()

    def permission_denied(self, request, message=None):
        if not request.successful_authenticator:
            raise exceptions.FamilySpaceException(**errorcodes.ERR_WRONG_TOKEN)
        super().permission_denied(request, message=None)


class CategoryEdit(CreateModelMixin, UpdateModelMixin, DestroyModelMixin,
                   viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, IsAdminUser,)
    renderer_classes = (ApiJSONRenderer,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    schema = CategoryEditSchema()

    def permission_denied(self, request, message=None):
        if not request.successful_authenticator:
            raise exceptions.FamilySpaceException(**errorcodes.ERR_WRONG_TOKEN)
        if not request.user.is_staff:
            raise exceptions.FamilySpaceException(**errorcodes.ERR_NO_RIGHTS_FOR_ACTION)
        super().permission_denied(request, message=None)


class GroupEdit(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,
                viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ApiJSONRenderer,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    schema = GroupEditSchema()

    def permission_denied(self, request, message=None):
        if not request.successful_authenticator:
            raise exceptions.FamilySpaceException(**errorcodes.ERR_WRONG_TOKEN)
        super().permission_denied(request, message=None)
