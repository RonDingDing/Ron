from rest_framework.serializers import FloatField, DateTimeField, SlugRelatedField
from ..baseserializer import DynamicFieldsModelSerializer
from ..models import Cost, CostType, Unit


class CostListRetrieveSerializer(DynamicFieldsModelSerializer):
    single_price = FloatField()
    price = FloatField()
    buy_time = DateTimeField(format="%Y-%m-%d %H:%M:%S")
    unit = SlugRelatedField(slug_field='name', read_only=True)
    costtype = SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Cost
        exclude = ['_price']


class CostCreateSerializer(DynamicFieldsModelSerializer):
    price = FloatField()
    class Meta:
        model = Cost
        exclude = ['state', '_price' ]

class CostUpdateSerializer(DynamicFieldsModelSerializer):
    buy_time = DateTimeField(format="%Y-%m-%d %H:%M:%S")
    price = FloatField()

    class Meta:
        model = Cost
        exclude = ['_price']

class CostTypeSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = CostType
        fields = '__all__'


class UnitSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'