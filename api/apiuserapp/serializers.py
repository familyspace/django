from rest_framework import serializers

from authapp.models import UserProfile
from api.core import errorcodes
from api.core import exceptions


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('gender', 'birth_date', 'id')
