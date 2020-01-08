from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .filterclass import CostTypeFilter, UnitFilter, CostFilter
from .serializers import CostListRetrieveSerializer, CostCreateSerializer, CostUpdateSerializer, CostTypeSerializer, \
    UnitSerializer
from ..baseviewset import NoDeleteNoModifyModelViewSet
from ..models import Cost, CostType, Unit


class CostViewSet(ModelViewSet):
    queryset = Cost.objects.order_by('-buy_time')
    filter_class = CostFilter
    def get_serializer_class(self):
        if self.action == 'create':
            return CostCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return CostUpdateSerializer
        return CostListRetrieveSerializer


class CostTypeViewSet(NoDeleteNoModifyModelViewSet):
    queryset = CostType.objects.order_by('pk')
    serializer_class = CostTypeSerializer
    filter_class = CostTypeFilter

    def perform_create(self, serializer):
        serializer.Meta.model.objects.get_or_create(**serializer.validated_data)


class UnitViewSet(NoDeleteNoModifyModelViewSet):
    queryset = Unit.objects.order_by('pk')
    serializer_class = UnitSerializer
    filter_class = UnitFilter

    def perform_create(self, serializer):
        serializer.Meta.model.objects.get_or_create(**serializer.validated_data)


class CostPlanViewSet(GenericViewSet):
    def list(self, request, *args, **kwargs):
        return Response({
            '支出': str(request._request._current_scheme_host) + '/cost/cost/',
            '支出类型': str(request._request._current_scheme_host) + '/cost/costtype/',
            '单位': str(request._request._current_scheme_host) + '/cost/unit/',
        })
