from django.shortcuts import render
from collections import OrderedDict
from django_filters import rest_framework as filters

from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, \
    RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated

from api.apichatapp.schemas import ChatSchema
from api.apichatapp.serializers import ChatSerializer
from api.core import errorcodes
from api.core import exceptions
from api.core.renderrers import ApiJSONRenderer
from chatapp.models import Chat


class ChatList(ListAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ApiJSONRenderer,)
    serializer_class = ChatSerializer
    schema = ChatSchema()

    def get_queryset(self):
        return Chat.objects.filter(group_id=self.kwargs['group_id'])

    def permission_denied(self, request, message=None):
        if not request.successful_authenticator:
            raise exceptions.FamilySpaceException(**errorcodes.ERR_WRONG_TOKEN)
        super().permission_denied(request, message=None)


class ChatViewSet(CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ApiJSONRenderer,)
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    schema = ChatSchema()

    def permission_denied(self, request, message=None):
        if not request.successful_authenticator:
            raise exceptions.FamilySpaceException(**errorcodes.ERR_WRONG_TOKEN)
        super().permission_denied(request, message=None)
