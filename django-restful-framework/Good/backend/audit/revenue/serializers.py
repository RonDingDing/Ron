from rest_framework.serializers import DateTimeField

from ..baseserializer import DynamicFieldsModelSerializer
from ..models import Order, Product


class ProductSmallSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

class OrderListRetrieveSerializer(DynamicFieldsModelSerializer):
    products = ProductSmallSerializer(read_only=True, many=True)
    sale_time = DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Order
        fields = '__all__'

class OrderCreateSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Order
        exclude = ['sale_time', 'state', 'revenue']