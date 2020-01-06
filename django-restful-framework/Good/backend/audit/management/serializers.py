from rest_framework.serializers import FloatField, DateTimeField
from ..baseserializer import DynamicFieldsModelSerializer
from ..models import CostType, ProductType, Product, Unit


class CostTypeSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = CostType
        fields = '__all__'


class ProductTypeSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class UnitSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class ProductCreateSerializer(DynamicFieldsModelSerializer):
    price = FloatField()

    def validate_price(self, price):
        return price * 100

    class Meta:
        model = Product
        exclude = ['_price', 'insert_time', 'old']


class ProductListRetrieveSerializer(DynamicFieldsModelSerializer):
    types = ProductTypeSerializer(read_only=True)
    insert_time = DateTimeField(format="%Y-%m-%d %H:%M:%S" )

    class Meta:
        model = Product
        fields = '__all__'
