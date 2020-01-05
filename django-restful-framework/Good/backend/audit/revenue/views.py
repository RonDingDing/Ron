from rest_framework.viewsets import ModelViewSet
from ..models import Order
from .serializers import OrderSerializer


class RevenueVueSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)