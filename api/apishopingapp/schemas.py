import coreapi
import coreschema
from rest_framework.schemas import AutoSchema


class ShopingSchema(AutoSchema):
    def get_description(self, path, method):
        if method == 'GET':
            return 'Получить список покупок'
        if method == 'POST':
            return 'Добавить покупку'
        if method == 'PUT':
            return 'Изменить покупку'
        if method == 'DELETE':
            return 'Удалить покупку'

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
                                             description="Название покупки"),
                    description='Название покупки',
                ),
                coreapi.Field(
                    name="price",
                    required=True,
                    location="form",
                    schema=coreschema.Number(title="price",
                                             description="Цена"),
                    description='Цена',
                ),
                coreapi.Field(
                    name="comment",
                    required=True,
                    location="form",
                    schema=coreschema.String(title="comment",
                                             description="Комментарий"),
                    description='Комментарий',
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
                                             description="Название покупки"),
                    description='Название покупки',
                ),
                coreapi.Field(
                    name="price",
                    required=True,
                    location="form",
                    schema=coreschema.Number(title="price",
                                             description="Цена"),
                    description='Цена',
                ),
                coreapi.Field(
                    name="comment",
                    required=True,
                    location="form",
                    schema=coreschema.String(title="comment",
                                             description="Комментарий"),
                    description='Комментарий',
                ),
            ]

        return fields
