from rest_framework import serializers

from api.core import errorcodes
from api.core import exceptions
from taskapp.models import Task


class TaskSerializer(serializers.ModelSerializer):
    group_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Task
        fields = ('id', 'group_id', 'title', 'done')
        read_only_fields = ('id',)
