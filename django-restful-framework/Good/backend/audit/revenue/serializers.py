from rest_framework.serializers import DateTimeField, SlugRelatedField, FloatField

from ..baseserializer import DynamicFieldsModelSerializer
from ..models import Order, Product,  ProductType


class ProductSmallSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']



class OrderListRetrieveSerializer(DynamicFieldsModelSerializer):
    revenue = FloatField()
    member = SlugRelatedField(slug_field='name', read_only=True)
    product = SlugRelatedField(slug_field='name', read_only=True)
    sale_time = DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Order
        exclude = ['id', ]

class OrderCreateSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Order
        exclude = ['sale_time', 'state']


class OrderUpdateSerializer(DynamicFieldsModelSerializer):
    sale_time = DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Order
        fields = '__all__'


class ProductTypeSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class ProductCreateSerializer(DynamicFieldsModelSerializer):
    price = FloatField()

    class Meta:
        model = Product
        exclude = ['_price', 'insert_time', 'old']


class ProductListRetrieveSerializer(DynamicFieldsModelSerializer):
    types = SlugRelatedField(slug_field='name', read_only=True)
    insert_time = DateTimeField(format="%Y-%m-%d %H:%M:%S")
    price = FloatField()

    class Meta:
        model = Product
        exclude = ['_price']
