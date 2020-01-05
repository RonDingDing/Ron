from rest_framework.viewsets import ModelViewSet
from ..models import CostType, ProductType, Product
from .serializers import CostTypeSerializer, ProductTypeSerializer, ProductSerializer
import time


class CostTypeViewSet(ModelViewSet):
    queryset = CostType.objects.all()
    serializer_class = CostTypeSerializer

    def create(self, request, *args, **kwargs):
        request.data['name'] = kwargs['name']
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.Meta.model.objects.get_or_create(**serializer.validated_data)


class ProducttypeViewSet(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

    def create(self, request, *args, **kwargs):
        request.data['name'] = kwargs['name']
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.Meta.model.objects.get_or_create(**serializer.validated_data)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.filter(old=False)
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):

        dic = {'name': kwargs['name'], '_price': int(kwargs['price'] * 100), 'types': kwargs['types'],
               'insert_time': int(time.time()), 'old': False}
        request.data.update(dic)
        response = super().create(request, *args, **kwargs)
        response.data['price'] = response.data.pop('_price') / 100
        return response

    def perform_create(self, serializer):
        filter_dic = {'name': serializer.validated_data['name']}
        serializer.Meta.model.objects.filter(**filter_dic).update(old=True)
        serializer.save()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        for i in response.data:
            i['price'] = i.pop('_price') / 100
        return response
