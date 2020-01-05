from ..baseserializer import DynamicFieldsModelSerializer
from ..models import Order

class OrderSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Order