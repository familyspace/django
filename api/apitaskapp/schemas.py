import coreapi
import coreschema
from rest_framework.schemas import AutoSchema


class TaskSchema(AutoSchema):
    def get_description(self, path, method):
        if method == 'GET':
            return 'Получить список задач'
        if method == 'POST':
            return 'Добавить задачу'
        if method == 'PUT':
            return 'Изменить задачу'
        if method == 'DELETE':
            return 'Удалить задачу'

    def get_encoding(self, path, method):
        return 'application/json'

    def get_serializer_fields(self, path, method):
        fields = []
        if method == 'POST':
            fields = [
                coreapi.Field(
                    name="group_id",
                    required=True,
                    location="form",
                    schema=coreschema.Integer(title="group",
                                              description="Id группы"),
                    description='group_id'
                ),
                coreapi.Field(
                    name="title",
                    required=True,
                    location="form",
                    schema=coreschema.String(title="title",
                                             description="Название задачи"),
                    description='Название задачи',
                ),
                coreapi.Field(
                    name="user",
                    required=True,
                    location="form",
                    schema=coreschema.Array(title="user",
                                             description="Юзеры в задаче"),
                    description='Юзеры в задаче',
                ),
            ]
        if method == 'PUT':
            fields = [
                coreapi.Field(
                    name="done",
                    required=True,
                    location="form",
                    schema=coreschema.Boolean(title="done",
                                              description="Завершено"),
                    description='Завершено'
                ),
                coreapi.Field(
                    name="title",
                    required=True,
                    location="form",
                    schema=coreschema.String(title="title",
                                             description="Название задачи"),
                    description='Название задачи',
                ),
                coreapi.Field(
                    name="user",
                    required=True,
                    location="form",
                    schema=coreschema.Array(title="user",
                                            description="Юзеры в задаче"),
                    description='Юзеры в задаче',
                ),
            ]

        return fields
