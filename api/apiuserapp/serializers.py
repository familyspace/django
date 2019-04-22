from rest_framework import serializers

from api.apigroupapp.serializers import GroupSerializer
from authapp.models import UserProfile, User
from groupapp.models import GroupUser
from api.core import errorcodes
from api.core import exceptions


class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.HiddenField(default='', required=False)

    class Meta:
        model = UserProfile
        fields = ('gender', 'birth_date', 'id', 'email',
                  'first_name', 'last_name', 'patronymic', 'phone', 'password')
        read_only_fields = ('id', 'password')

    def update(self, instance, validated_data):
        # почему то он даёт изменять других пользователей и без проверки
        # if self.context['request'].user.id != self.initial_data['id']:
        #     raise exceptions.FamilySpaceException(**errorcodes.ERR_NO_RIGHTS_FOR_ACTION)
        if 'email' in self.initial_data:
            self.context['request'].user.email = self.initial_data['email']
        if 'password' in self.initial_data and self.initial_data['password']:
            self.context['request'].user.set_password(self.initial_data['password'])
        self.context['request'].user.save()
        return super().update(instance, validated_data)


class ContactListSerializer(serializers.ModelSerializer):
    contact_user = UserProfileSerializer()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserProfile
        fields = ('id', 'contact_user', 'user')
        read_only_fields = ('id',)


class GetUserGroupsSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)

    class Meta:
        model = GroupUser
        fields = ['group']
