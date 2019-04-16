from rest_framework import serializers

from api.apigroupapp.serializers import GroupSerializer
from authapp.models import UserProfile, User
from groupapp.models import GroupUser
from api.core import errorcodes
from api.core import exceptions


class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.HiddenField(default='')

    class Meta:
        model = UserProfile
        fields = ('gender', 'birth_date', 'id', 'email',
                  'first_name', 'last_name', 'patronymic', 'phone', 'password')
        read_only_fields = ('id', 'password')

    def update(self, instance, validated_data):
        # if self.context['request'].user.id != self.initial_data['id']:
        #     raise exceptions.FamilySpaceException(**errorcodes.ERR_NO_RIGHTS_FOR_ACTION)
        self.context['request'].user.email = self.initial_data['email']
        if self.initial_data['password']:
            res = self.context['request'].user.set_password(self.initial_data['password'])
        self.context['request'].user.save()
        return super().update(instance, validated_data)


class GetUserGroupsSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)

    class Meta:
        model = GroupUser
        fields = ['group']
