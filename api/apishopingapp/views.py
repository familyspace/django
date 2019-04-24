from django.shortcuts import render
from collections import OrderedDict
from django_filters import rest_framework as filters

from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, \
    RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated

from api.apichatapp.serializers import ChatSerializer
from api.apishopingapp.schemas import ShopingSchema
from api.apishopingapp.serializers import ShopingSerializer
from api.apitaskapp.schemas import TaskSchema
from api.apitaskapp.serializers import TaskSerializer
from api.core import errorcodes
from api.core import exceptions
from api.core.renderrers import ApiJSONRenderer
from shoppingapp.models import ShopingItem
from taskapp.models import Task


class ShopingList(ListAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ApiJSONRenderer,)
    serializer_class = ShopingSerializer
    schema = ShopingSchema()

    def get_queryset(self):
        return ShopingItem.objects.filter(group_id=self.kwargs['group_id'])

    def permission_denied(self, request, message=None):
        if not request.successful_authenticator:
            raise exceptions.FamilySpaceException(**errorcodes.ERR_WRONG_TOKEN)
        super().permission_denied(request, message=None)


class ShopingViewSet(CreateModelMixin, UpdateModelMixin, DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ApiJSONRenderer,)
    queryset = ShopingItem.objects.all()
    serializer_class = ShopingSerializer
    schema = ShopingSchema()

    def permission_denied(self, request, message=None):
        if not request.successful_authenticator:
            raise exceptions.FamilySpaceException(**errorcodes.ERR_WRONG_TOKEN)
        super().permission_denied(request, message=None)
