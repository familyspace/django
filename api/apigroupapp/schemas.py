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


class CategorySchema(AutoSchema):
    def get_description(self, path, method):
        if method == 'GET':
            return 'Получить список категорий'

    def get_encoding(self, path, method):
        return 'application/json'


class GroupSearchSchema(AutoSchema):
    def get_description(self, path, method):
        if method == 'GET':
            return 'Поиск групп'

    def get_encoding(self, path, method):
        return 'application/json'

    # поля добавляет фильтр

    # def get_serializer_fields(self, path, method):
    #     fields = []
    #     if method == 'GET':
    #         fields = [
    #             coreapi.Field(
    #                 name='search',
    #                 required=False,
    #                 location="query",
    #                 schema=coreschema.String(title='search',
    #                                          default=1,
    #                                          description='Строка поиска по названию группы'),
    #                 description='Строка поиска по названию группы'
    #             ),
    #             coreapi.Field(
    #                 name='category',
    #                 required=False,
    #                 location="query",
    #                 schema=coreschema.Integer(title='category',
    #                                          default=1,
    #                                          description='Фильтр по категориям'),
    #                 description='Фильтр по категориям'
    #             ),
    #         ]
    #     return fields


class CategoryEditSchema(AutoSchema):
    def get_description(self, path, method):
        if method == 'PUT':
            return 'Изменить категорию'
        if method == 'DELETE':
            return 'Удалить удалить категорию'
        if method == 'POST':
            return 'Добавить категорию'

    def get_encoding(self, path, method):
        return 'application/json'

    def get_serializer_fields(self, path, method):
        fields = []
        if method == 'PUT' or method == 'POST':
            fields = [
                coreapi.Field(
                    name="name",
                    required=True,
                    location="form",
                    schema=coreschema.String(title="name",
                                             description="name"),
                    description='Название категории',
                ),
            ]

        return fields


class GroupEditSchema(AutoSchema):
    def get_description(self, path, method):
        if method == 'POST':
            return 'Создать группу'
        if method == 'PUT':
            return 'Изменить группу по её id'
        if method == 'GET':
            return 'Просмотреть детали группы по её id'

    def get_encoding(self, path, method):
        return 'application/json'

    def get_serializer_fields(self, path, method):
        fields = []
        if method in ['PUT', 'POST']:
            fields = [
                coreapi.Field(
                    name="title",
                    required=True,
                    location="form",
                    schema=coreschema.String(title="title",
                                             description="title"),
                    description='Название группы',
                ),
                coreapi.Field(
                    name="description",
                    required=True,
                    location="form",
                    schema=coreschema.String(title="description",
                                             description="description"),
                    description='Описание',
                ),
                coreapi.Field(
                    name="category",
                    required=True,
                    location="form",
                    schema=coreschema.Integer(title="category",
                                              description="category"),
                    description='ID категории',
                ),
                coreapi.Field(
                    name="is_public",
                    required=True,
                    location="form",
                    schema=coreschema.Boolean(title="is_public",
                                              description="is_public"),
                    description='Группа публичная',
                ),

            ]

        return fields
