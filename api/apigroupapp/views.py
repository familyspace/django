from django.shortcuts import render
from collections import OrderedDict

from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated

from api.apigroupapp.schemas import UsersGroupsSchema
from api.apigroupapp.serializers import UsersGroupsSerializer
from api.core import errorcodes
from api.core import exceptions
from api.core.renderrers import ApiJSONRenderer

from groupapp.models import GroupUser


class UsersGroups(CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin,
                           viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ApiJSONRenderer,)
    serializer_class = UsersGroupsSerializer
    schema = UsersGroupsSchema()

    def get_queryset(self):
        print(self.request)
        return GroupUser.objects.all()#filter(user=self.request.user.pk)

    def permission_denied(self, request, message=None):
        if not request.successful_authenticator:
            raise exceptions.FamilySpaceException(**errorcodes.ERR_WRONG_TOKEN)
        super().permission_denied(request, message=None)
