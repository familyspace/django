import coreapi
import coreschema
from rest_framework.schemas import AutoSchema


class ViewedSchema(AutoSchema):
    def get_description(self, path, method):
        if method == 'GET':
            return 'Получить профаил пользователя'
        if method in ['PUT', 'PATCH']:
            return 'Изменить профаил пользователя'

    def get_encoding(self, path, method):
        return 'application/json'

    def get_serializer_fields(self, path, method):
        fields = []
        if method == 'PUT':
            fields = [
                coreapi.Field(
                    name='gender',
                    required=True,
                    location="form",
                    schema=coreschema.String(title='gender',
                                             default=1,
                                             description='user_gender'),
                    description='варианты M W'
                ),
                coreapi.Field(
                    name='birth_date',
                    required=True,
                    location="form",
                    schema=coreschema.String(title='birth_date',
                                             default='false',
                                             description='birth_date'),
                    description='формат  YYYY-MM-DD'
                ),
            ]

        return fields


class GetUserGroupsSchema(AutoSchema):
    def get_description(self, path, method):
        if method == 'GET':
            return 'Получить группы пользователя'

    def get_encoding(self, path, method):
        return 'application/json'

