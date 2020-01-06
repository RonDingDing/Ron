from rest_framework.serializers import FloatField
from ..baseserializer import DynamicFieldsModelSerializer
from ..models import Cost


class CostListRetrieveSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Cost
        fields = '__all__'


class CostCreateSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Cost
        exclude = ['single_price']
