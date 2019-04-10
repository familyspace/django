from django.core.serializers import json
from django.http import JsonResponse
from rest_framework import serializers

from api.apigroupapp.serializers import GroupSerializer
from authapp.models import UserProfile, User
from api.core import errorcodes
from api.core import exceptions
from groupapp.models import GroupUser, Group


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('gender', 'birth_date', 'id')


class UsersGroupsSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)

    class Meta:
        model = GroupUser
        fields = ['group']

