from rest_framework.response import Response
from rest_framework.viewsets import   GenericViewSet
from restframework_datachange.viewsets import RModelViewSet

from .serializers import OrderListRetrieveSerializer, OrderCreateSerializer, OrderUpdateSerializer, \
    ProductTypeSerializer, ProductCreateSerializer, ProductListRetrieveSerializer
from ..baseviewset import NoDeleteNoModifyModelViewSet
from ..models import Order, Product, ProductType
from .filterclass import ProductFilter, ProductTypeFilter, OrderFilter


class RevenueAdjust:
    def relist_data(self, data):
        lst = []
        for order_id in {i['order_id'] for i in data}:
            all_products = []
            revenue = 0
            objs = [i for i in data if i['order_id'] == order_id]
            for obj in objs:
                all_products.append({'number': obj['number'],
                                     'product': obj['product']})
                revenue += obj['revenue']
            dic = {'order_id': order_id, 'all_products': all_products, 'sale_time': objs[0]['sale_time'],
               'state': objs[0]['state'], 'discount': objs[0]['discount'], 'member': objs[0]['member'],
               'revenue': revenue
               }
            lst.append(dic)

        return lst


class RevenueViewSet(RevenueAdjust, RModelViewSet):
    queryset = Order.objects.order_by('-sale_time')
    filter_class = OrderFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return OrderUpdateSerializer
        return OrderListRetrieveSerializer

    def perform_create(self, serializer):
        product = serializer.validated_data['product']
        order_id = serializer.validated_data['order_id']
        number = serializer.validated_data['number']
        found = False
        for obj in serializer.Meta.model.objects.filter(order_id=order_id):
            if obj.product == product:
                obj.number += number
                obj.save()
                found = True
        if not found:
            serializer.save()

class ProducttypeViewSet(NoDeleteNoModifyModelViewSet):
    queryset = ProductType.objects.order_by('pk')
    serializer_class = ProductTypeSerializer
    filter_class = ProductTypeFilter

    def perform_create(self, serializer):
        serializer.Meta.model.objects.get_or_create(**serializer.validated_data)


class ProductViewSet(NoDeleteNoModifyModelViewSet):
    queryset = Product.objects.filter(old=False).order_by('-insert_time')
    filter_class = ProductFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return ProductCreateSerializer
        return ProductListRetrieveSerializer

    def perform_create(self, serializer):
        filter_dic = {'name': serializer.validated_data['name']}
        serializer.Meta.model.objects.filter(**filter_dic).update(old=True)
        serializer.save()


class ProductPlanViewSet(GenericViewSet):
    def list(self, request, *args, **kwargs):
        return Response({

            '收入': str(request._request._current_scheme_host) + '/revenue/revenue/',
            '产品': str(request._request._current_scheme_host) + '/revenue/product/',
            '产品类型': str(request._request._current_scheme_host) + '/revenue/producttype/',

        })
