from django.shortcuts import render
from collections import OrderedDict

from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated

from api.core import errorcodes
from api.core import exceptions
from api.core.renderrers import ApiJSONRenderer
from authapp.models import UserProfile, User, UserContactList
from api.apiuserapp.schemas import UserProfileSchema, GetUserGroupsSchema, UserSearchSchema, ContactListSchema
from api.apiuserapp.serializers import UserProfileSerializer, GetUserGroupsSerializer, ContactListSerializer

# Create your views here.
from groupapp.models import GroupUser


class UserProfileViewSet(ListModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ApiJSONRenderer,)
    serializer_class = UserProfileSerializer
    schema = UserProfileSchema()

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

    def permission_denied(self, request, message=None):
        if not request.successful_authenticator:
            raise exceptions.FamilySpaceException(**errorcodes.ERR_WRONG_TOKEN)
        super().permission_denied(request, message=None)


class GetUserGroups(ListAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ApiJSONRenderer,)
    serializer_class = GetUserGroupsSerializer
    schema = GetUserGroupsSchema()

    def get_queryset(self):
        return GroupUser.objects.filter(user=self.request.user.pk)

    def permission_denied(self, request, message=None):
        if not request.successful_authenticator:
            raise exceptions.FamilySpaceException(**errorcodes.ERR_WRONG_TOKEN)
        super().permission_denied(request, message=None)


class UserSearchFilter(filters.FilterSet):
    # TODO не работает регистронезависимый поиск
    search = filters.CharFilter(field_name="email", lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['search', ]


class UserSearch(ListAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ApiJSONRenderer,)
    serializer_class = UserProfileSerializer
    schema = UserSearchSchema()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserSearchFilter

    def get_queryset(self):
        # проверка наличия параметра search в адрессе запроса
        if not 'search' in self.request.query_params:
            # если его нет возвращаю пустой набор
            return User.objects.filter(pk=-1)

        return User.objects.all().exclude(pk=self.request.user.pk)

    def permission_denied(self, request, message=None):
        if not request.successful_authenticator:
            raise exceptions.FamilySpaceException(**errorcodes.ERR_WRONG_TOKEN)
        super().permission_denied(request, message=None)


class ContactListViewSet(ListModelMixin, DestroyModelMixin, CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ApiJSONRenderer,)
    serializer_class = ContactListSerializer
    schema = ContactListSchema()

    def get_queryset(self):
        return UserContactList.objects.filter(user=self.request.user)

    def permission_denied(self, request, message=None):
        if not request.successful_authenticator:
            raise exceptions.FamilySpaceException(**errorcodes.ERR_WRONG_TOKEN)
        super().permission_denied(request, message=None)
