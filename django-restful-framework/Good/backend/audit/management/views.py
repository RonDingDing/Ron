from ..models import CostType, ProductType, Product, Unit
from .serializers import CostTypeSerializer, ProductTypeSerializer, ProductCreateSerializer, ProductListRetrieveSerializer, UnitSerializer
import datetime
from restframework_datachange.viewsets import RModelViewSet
from pytz import timezone
from django.conf import settings

class CostTypeViewSet(RModelViewSet):
    queryset = CostType.objects.all()
    serializer_class = CostTypeSerializer

    def perform_create(self, serializer):
        serializer.Meta.model.objects.get_or_create(**serializer.validated_data)


class ProducttypeViewSet(RModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

    def perform_create(self, serializer):
        serializer.Meta.model.objects.get_or_create(**serializer.validated_data)



class ProductAdjust(object):
    list_exclude = ['_price']
    price_src1 = '_price'

    def add_price(self, _price):
        return _price / 100

    def change_insert_time(self, value):
        timetuple = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        local_time = timezone(settings.TIME_ZONE).localize(timetuple)
        time_string = local_time.strftime('%Y-%m-%d %H:%M:%S')
        return time_string

class ProductViewSet(ProductAdjust, RModelViewSet):
    queryset = Product.objects.filter(old=False)

    def get_serializer_class(self):
        if self.action == 'create':
            return ProductCreateSerializer
        return ProductListRetrieveSerializer

    def perform_create(self, serializer):
        filter_dic = {'name': serializer.validated_data['name']}
        serializer.Meta.model.objects.filter(**filter_dic).update(old=True)
        serializer.save()


class UnitViewSet(RModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    def perform_create(self, serializer):
        serializer.Meta.model.objects.get_or_create(**serializer.validated_data)