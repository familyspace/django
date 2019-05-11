from rest_framework import serializers

from api.core import errorcodes
from api.core import exceptions
from eventapp.models import Event
from taskapp.models import Task


class EventSerializer(serializers.ModelSerializer):
    group_id = serializers.IntegerField(write_only=True, required=False)
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    location = serializers.CharField(required=False)
    date = serializers.DateTimeField(required=False)


    class Meta:
        model = Event
        fields = ('id', 'group_id', 'title', 'description', 'location', 'date',)
        read_only_fields = ('id',)
