import coreapi
import coreschema
from rest_framework.schemas import AutoSchema


class ChatSchema(AutoSchema):
    def get_description(self, path, method):
        if method == 'GET':
            return 'Получить список сообщений'
        if method == 'POST':
            return 'Добавить сообщение'

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
                    name="text",
                    required=True,
                    location="form",
                    schema=coreschema.String(title="Text",
                                             description="Текст"),
                    description='Текст сообщения',
                ),
            ]


        return fields

