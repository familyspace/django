from rest_framework import serializers

from chatapp.models import Chat
from api.core import errorcodes
from api.core import exceptions


class ChatSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    group_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Chat
        fields = ('id', 'group_id', 'user_id', 'date_modify', 'date_create', 'user', 'text',)
        read_only_fields = ('id', 'date_modify', 'date_create', 'user_id',)

    def create(self, validated_data):
        user = validated_data['user']

        return super().create(validated_data)
