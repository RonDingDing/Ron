from ..baseserializer import DynamicFieldsModelSerializer
from rest_framework.serializers import DateTimeField, SlugField
from ..models import Order, Product
from audit.management.serializers import ProductListRetrieveSerializer

class OrderListRetrieveSerializer(DynamicFieldsModelSerializer):
    products = ProductListRetrieveSerializer(read_only=True, many=True)
    sale_time = DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Order
        fields = '__all__'

class OrderCreateSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Order
        exclude = ['sale_time', 'state', 'revenue']