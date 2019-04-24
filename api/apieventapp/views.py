from django.shortcuts import render
from collections import OrderedDict
from django_filters import rest_framework as filters

from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, \
    RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated

from api.apieventapp.schemas import EventSchema
from api.apieventapp.serializers import EventSerializer
from api.core import errorcodes
from api.core import exceptions
from api.core.renderrers import ApiJSONRenderer
from eventapp.models import Event


class EventList(ListAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ApiJSONRenderer,)
    serializer_class = EventSerializer
    schema = EventSchema()

    def get_queryset(self):
        return Event.objects.filter(group_id=self.kwargs['group_id'])

    def permission_denied(self, request, message=None):
        if not request.successful_authenticator:
            raise exceptions.FamilySpaceException(**errorcodes.ERR_WRONG_TOKEN)
        super().permission_denied(request, message=None)


class EventViewSet(CreateModelMixin, UpdateModelMixin, DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (ApiJSONRenderer,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    schema = EventSchema()

    def permission_denied(self, request, message=None):
        if not request.successful_authenticator:
            raise exceptions.FamilySpaceException(**errorcodes.ERR_WRONG_TOKEN)
        super().permission_denied(request, message=None)
