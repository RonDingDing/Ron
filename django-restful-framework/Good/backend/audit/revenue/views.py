from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .serializers import OrderListRetrieveSerializer, OrderCreateSerializer, OrderUpdateSerializer, \
    ProductTypeSerializer, ProductCreateSerializer, ProductListRetrieveSerializer
from ..baseviewset import NoDeleteNoModifyModelViewSet
from ..models import Order, Product, ProductType


class RevenueViewSet(ModelViewSet):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return OrderUpdateSerializer
        return OrderListRetrieveSerializer


class ProducttypeViewSet(NoDeleteNoModifyModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

    def perform_create(self, serializer):
        serializer.Meta.model.objects.get_or_create(**serializer.validated_data)


class ProductViewSet(NoDeleteNoModifyModelViewSet):
    queryset = Product.objects.filter(old=False)

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
