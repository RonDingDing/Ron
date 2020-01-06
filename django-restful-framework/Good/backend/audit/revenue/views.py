from restframework_datachange.viewsets import RModelViewSet
from ..models import Order
from .serializers import OrderListRetrieveSerializer, OrderCreateSerializer
import datetime
from pytz import timezone
from django.conf import settings

class RevenueAdjust(object):
    def change_sale_time(self, value):

        timetuple = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        local_time = timezone(settings.TIME_ZONE).localize(timetuple)
        time_string = local_time.strftime('%Y-%m-%d %H:%M:%S')
        return time_string

class RevenueViewSet(RevenueAdjust, RModelViewSet):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        return OrderListRetrieveSerializer

    def perform_create(self, serializer):
        dic = {'revenue': sum(product.price for product in serializer.validated_data['products'])}
        serializer.validated_data.update(dic)
        serializer.save()