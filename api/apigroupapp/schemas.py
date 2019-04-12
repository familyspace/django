import coreapi
import coreschema
from rest_framework.schemas import AutoSchema


class UsersGroupsSchema(AutoSchema):
    def get_description(self, path, method):
        if method == 'GET':
            return 'Получить список пользователей в группе'
        if method == 'PUT':
            return 'Изменить роль в группе'
        if method == 'DELETE':
            return 'Удалить пользователя в группе'
        if method == 'POST':
            return 'Добавить пользователя в группу'

    def get_encoding(self, path, method):
        return 'application/json'

    def get_serializer_fields(self, path, method):
        fields = []
        if method == 'GET':
            fields = [
                coreapi.Field(
                    name='group_id',
                    required=False,
                    location="query",
                    schema=coreschema.String(title='id',
                                             default=1,
                                             description='id группы'),
                    description='id группы'
                ),
            ]
        if method == 'POST':
            fields = [
                coreapi.Field(
                    name="user_id",
                    required=True,
                    location="form",
                    schema=coreschema.Integer(title="user_id",
                                             description="Id пользователя"),
                    description='user_id'
                ),
                coreapi.Field(
                    name="group_id",
                    required=True,
                    location="form",
                    schema=coreschema.Integer(title="group_id",
                                              description="Id группы"),
                    description='group_id'
                ),
                coreapi.Field(
                    name="role",
                    required=True,
                    location="form",
                    schema=coreschema.String(title="role",
                                              description="Роль"),
                    description='Значение ADM или USR',
                ),
            ]
        if method == 'PUT':
            fields = [
                coreapi.Field(
                    name="role",
                    required=True,
                    location="form",
                    schema=coreschema.String(title="role",
                                             description="Роль"),
                    description='Значение ADM или USR',
                ),
            ]

        return fields
