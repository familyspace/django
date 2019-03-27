import coreapi
import coreschema
from rest_framework.schemas import AutoSchema


class CustomersSchema(AutoSchema):
    def get_description(self, path, method):

        if path == '/apiauth/signup/':
            return 'Создание нового пользователя.'
        if path == '/apiauth/signin/':
            return 'Авторизация по логину и паролю.'

        return None

    def get_encoding(self, path, method):
        return 'application/json'

    def get_serializer_fields(self, path, method):
        fields = []
        if method == 'POST':
            fields = [
                coreapi.Field(
                    "login",
                    required=True,
                    location="form",
                    schema=coreschema.String(title="Username",
                                             description="Valid username for authentication"),
                    description='username'
                ),
                coreapi.Field(
                    "password",
                    required=True,
                    location="form",
                    schema=coreschema.String(),
                    description='Password in sha256, for example '
                                '8D969EEF6ECAD3C29A3A629280E686CF0C3F5D5A86AFF3CA12020C923ADC6C92',
                ),
            ]
        return fields
