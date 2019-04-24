import coreapi
import coreschema
from rest_framework.schemas import AutoSchema


class EventSchema(AutoSchema):
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
                    name="description",
                    required=True,
                    location="form",
                    schema=coreschema.String(title="description",
                                             description="Описание"),
                    description='Описание',
                ),
                coreapi.Field(
                    name="location",
                    required=True,
                    location="form",
                    schema=coreschema.String(title="location",
                                             description="Место проведения"),
                    description='Место проведения',
                ),
                coreapi.Field(
                    name="date",
                    required=True,
                    location="form",
                    schema=coreschema.String(title="date",
                                             description="Дата и время"),
                    description='Дата и время',
                ),
            ]
        if method == 'PUT':
            fields = [
                coreapi.Field(
                    name="title",
                    required=True,
                    location="form",
                    schema=coreschema.String(title="title",
                                             description="Название задачи"),
                    description='Название задачи',
                ),
                coreapi.Field(
                    name="description",
                    required=True,
                    location="form",
                    schema=coreschema.String(title="description",
                                             description="Описание"),
                    description='Описание',
                ),
                coreapi.Field(
                    name="location",
                    required=True,
                    location="form",
                    schema=coreschema.String(title="location",
                                             description="Место проведения"),
                    description='Место проведения',
                ),
                coreapi.Field(
                    name="date",
                    required=True,
                    location="form",
                    schema=coreschema.String(title="date",
                                             description="Дата и время"),
                    description='Дата и время',
                ),
            ]

        return fields
