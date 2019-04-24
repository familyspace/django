from rest_framework import serializers

from api.core import errorcodes
from api.core import exceptions
from shoppingapp.models import ShopingItem
from taskapp.models import Task


class ShopingSerializer(serializers.ModelSerializer):
    group_id = serializers.IntegerField(write_only=True, required=False)
    done = serializers.BooleanField(required=False)
    price = serializers.DecimalField(max_digits=9, decimal_places=2, required=False)
    comment = serializers.CharField(required=False)

    class Meta:
        model = ShopingItem
        fields = ('id', 'group_id', 'title', 'done', 'price', 'comment')
        read_only_fields = ('id',)
