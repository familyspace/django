from rest_framework import serializers

from groupapp.models import Group, GroupUser


class GroupSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ['id', 'title', 'description', 'is_public', 'category']

    def get_category(self, obj):
        return obj.category.name


class UsersGroupsSerializer(serializers.ModelSerializer):
    # role = serializers.SerializerMethodField()
    group_id = serializers.IntegerField(required=False)
    user_id = serializers.IntegerField(required=False)

    class Meta:
        model = GroupUser
        fields = ['id', 'user_id', 'role', 'group_id']

    # def get_role(self, obj):
    #     print(type(obj.role))
    #     return obj.role
