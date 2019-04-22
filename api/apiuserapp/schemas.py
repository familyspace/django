import coreapi
import coreschema
from rest_framework.schemas import AutoSchema


class UserProfileSchema(AutoSchema):
    def get_description(self, path, method):
        if method == 'GET':
            return 'Получить профаил пользователя'
        if method in ['PUT', 'PATCH']:
            return 'Изменить профаил пользователя'

    def get_encoding(self, path, method):
        return 'application/json'

    def get_serializer_fields(self, path, method):
        fields = []
        if method in ['PUT', 'PATCH']:
            fields = [
                coreapi.Field(
                    name='gender',
                    required=False,
                    location="form",
                    schema=coreschema.String(title='gender',
                                             description='user_gender'),
                    description='варианты M W'
                ),
                coreapi.Field(
                    name='birth_date',
                    required=False,
                    location="form",
                    schema=coreschema.String(title='birth_date',
                                             description='birth_date'),
                    description='формат  YYYY-MM-DD'
                ),
                coreapi.Field(
                    name='email',
                    required=False,
                    location="form",
                    schema=coreschema.String(title='email',
                                             description='email'),
                    description='email'
                ),
                coreapi.Field(
                    name='first_name',
                    required=False,
                    location="form",
                    schema=coreschema.String(title='first_name',
                                             description='first_name'),
                    description='Имя'
                ),
                coreapi.Field(
                    name='last_name',
                    required=False,
                    location="form",
                    schema=coreschema.String(title='last_name',
                                             description='last_name'),
                    description='Фамилия'
                ),
                coreapi.Field(
                    name='patronymic',
                    required=False,
                    location="form",
                    schema=coreschema.String(title='patronymic',
                                             description='patronymic'),
                    description='Отчество'
                ),
                coreapi.Field(
                    name='phone',
                    required=False,
                    location="form",
                    schema=coreschema.String(title='Phone',
                                             description='Phone'),
                    description='Телефон'
                ),
                coreapi.Field(
                    name='password',
                    required=False,
                    location="form",
                    schema=coreschema.String(title='password',
                                             description='password'),
                    description='Новый пароль'
                ),

            ]

        return fields


class GetUserGroupsSchema(AutoSchema):
    def get_description(self, path, method):
        if method == 'GET':
            return 'Получить группы пользователя'

    def get_encoding(self, path, method):
        return 'application/json'


class UserSearchSchema(AutoSchema):
    def get_description(self, path, method):
        if method == 'GET':
            return 'Поиск пользователя'

    def get_encoding(self, path, method):
        return 'application/json'


class ContactListSchema(AutoSchema):
    def get_description(self, path, method):
        if method == 'GET':
            return 'Получить список контактов'
        if method == 'DELETE':
            return 'Удалить запись из контактов'
        if method == 'POST':
            return 'Добавить контакт'

    def get_encoding(self, path, method):
        return 'application/json'

    def get_serializer_fields(self, path, method):
        fields = []
        if method == 'POST':
            fields = [
                coreapi.Field(
                    name='user_id',
                    required=True,
                    location="form",
                    schema=coreschema.Integer(title='user_id',
                                              description='user_id'),
                    description='ID пользователя'
                ),
            ]

        return fields
