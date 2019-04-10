from rest_framework import serializers

from api.apigroupapp.serializers import GroupSerializer
from authapp.models import UserProfile, User
from api.core import errorcodes
from api.core import exceptions
from groupapp.models import GroupUser


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('gender', 'birth_date', 'id')


class UsersGroupsSerializer(serializers.ModelSerializer):
    groups = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'groups')

    def get_groups(self, obj):
        user_groups = [item for sublist in
                       GroupUser.objects.filter(user=self.context['request'].user).values('group') for item in
                       sublist]
        return GroupSerializer(instance=user_groups)
