from restframework_datachange.viewsets import RModelViewSet
from ..models import Order, Product, Item
from .serializers import OrderListRetrieveSerializer, OrderCreateSerializer
import datetime
from collections import defaultdict
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

    # def create(self, request, *args, **kwargs):
    #     cart_dic = defaultdict(int)
    #     revenue = 0
    #     for i in request.data['cart']:
    #         has_product = Product.objects.filter(pk=i)
    #         if has_product:
    #             product = has_product.first()
    #             cart_dic[product.id] += 1
    #             revenue += product.price
    #
    #     obj = Order(revenue=revenue)
    #     for k, v in cart_dic.items():
    #         obj.cart.add(Item.objects.create(product=k, number=v))
    #     obj.save()





