from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, IntegerField
from ..models import CostType, ProductType, Product
from ..baseserializer import DynamicFieldsModelSerializer



class CostTypeSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = CostType
        fields = '__all__'


class ProductTypeSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class ProductSerializer(DynamicFieldsModelSerializer):
    types = PrimaryKeyRelatedField(queryset=ProductType.objects.all())
    
    class Meta:
        model = Product
        fields = '__all__'
