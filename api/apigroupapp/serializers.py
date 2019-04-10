from rest_framework import serializers

from authapp.models import UserProfile, User
from api.core import errorcodes
from api.core import exceptions
from groupapp.models import Group


class GroupSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ['id', 'title', 'description', 'is_public', 'category']

    def get_category(self, obj):
        return obj.category.name
