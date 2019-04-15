from rest_framework import serializers

from authapp.models import User, UserProfile
from groupapp.models import Group, GroupUser, RoleChoice, Category
from api.core import errorcodes
from api.core import exceptions


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class GroupSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ['id', 'title', 'description', 'is_public', 'category_name', 'category']

    def get_category_name(self, obj):
        return obj.category.name


class UserSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()
    birth_date = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    patronymic = serializers.SerializerMethodField()
    phone = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'gender', 'birth_date', 'email',
                  'first_name', 'last_name', 'patronymic', 'phone')

    def get_gender(self, obj):
        return obj.userprofile.gender

    def get_birth_date(self, obj):
        return str(obj.userprofile.birth_date)

    def get_email(self, obj):
        return str(obj.userprofile.email)

    def get_first_name(self, obj):
        return str(obj.userprofile.first_name)

    def get_last_name(self, obj):
        return str(obj.userprofile.last_name)

    def get_patronymic(self, obj):
        return str(obj.userprofile.patronymic)

    def get_phone(self, obj):
        return str(obj.userprofile.phone)




class UsersGroupsSerializer(serializers.ModelSerializer):
    group_id = serializers.IntegerField(required=False)
    user_id = serializers.IntegerField(required=False)
    user = UserSerializer(read_only=True)

    class Meta:
        model = GroupUser
        fields = ['id', 'user_id', 'role', 'group_id', 'user']

    def create(self, validated_data):
        # проверяю права пользователя на добавление участника группы
        if not (GroupUser.objects.filter(user=self.context['request'].user,
                                         group=validated_data['group_id'],
                                         role=RoleChoice.ADM.name)):
            raise exceptions.FamilySpaceException(**errorcodes.ERR_NO_RIGHTS_FOR_ACTION)
        # проверяю есть ли уже пользователь в группе
        if GroupUser.objects.filter(user=validated_data['user_id'],
                                    group=validated_data['group_id']):
            raise exceptions.FamilySpaceException(**errorcodes.ERR_USER_ALREDY_IN_GROUP)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # проверяю права пользователя на изменение прав участника группы
        if not (GroupUser.objects.filter(user=self.context['request'].user,
                                         group=instance.group,
                                         role=RoleChoice.ADM.name)):
            raise exceptions.FamilySpaceException(**errorcodes.ERR_NO_RIGHTS_FOR_ACTION)
        return super().update(instance, validated_data)
