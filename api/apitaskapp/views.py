from django.shortcuts import render
from collections import OrderedDict
from django_filters import rest_framework as filters

from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, \
    RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated

from api.apichatapp.serializers import ChatSerializer
from api.apitaskapp.schemas import TaskSchema
from api.apitaskapp.serializers import TaskSerializer
from api.core import errorcodes
from api.core import exceptions
from api.core.renderrers import ApiJSONRenderer
from taskapp.models import Task


class TaskList(ListAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ApiJSONRenderer,)
    serializer_class = TaskSerializer
    schema = TaskSchema()

    def get_queryset(self):
        return Task.objects.filter(group_id=self.kwargs['group_id'])

    def permission_denied(self, request, message=None):
        if not request.successful_authenticator:
            raise exceptions.FamilySpaceException(**errorcodes.ERR_WRONG_TOKEN)
        super().permission_denied(request, message=None)


class TaskViewSet(CreateModelMixin, UpdateModelMixin, DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ApiJSONRenderer,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    schema = TaskSchema()

    def permission_denied(self, request, message=None):
        if not request.successful_authenticator:
            raise exceptions.FamilySpaceException(**errorcodes.ERR_WRONG_TOKEN)
        super().permission_denied(request, message=None)
