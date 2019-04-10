from django.shortcuts import render
from collections import OrderedDict

from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated

from api.core import errorcodes
from api.core import exceptions
from api.core.renderrers import ApiJSONRenderer
from authapp.models import UserProfile, User
from api.apiuserapp.schemas import ViewedSchema, UsersGroupsSchema
from api.apiuserapp.serializers import UserProfileSerializer, UsersGroupsSerializer


# Create your views here.
class UserProfileViewSet(ListModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ApiJSONRenderer,)
    serializer_class = UserProfileSerializer
    schema = ViewedSchema()

    def get_queryset(self):
            return UserProfile.objects.filter(user=self.request.user)


    def permission_denied(self, request, message=None):
        if not request.successful_authenticator:
            raise exceptions.FamilySpaceException(**errorcodes.ERR_WRONG_TOKEN)
        super().permission_denied(request, message=None)

class UsersGroups(ListAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ApiJSONRenderer,)
    serializer_class = UsersGroupsSerializer
    schema = UsersGroupsSchema()

    def get_queryset(self):
        return User.objects.filter(user=self.request.user)

    def permission_denied(self, request, message=None):
        if not request.successful_authenticator:
            raise exceptions.FitsMeException(**errorcodes.ERR_WRONG_TOKEN)
        super().permission_denied(request, message=None)