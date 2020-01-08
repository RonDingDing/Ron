from django_filters import rest_framework as filters, CharFilter, DateTimeFromToRangeFilter, RangeFilter

from ..models import CostType, Unit, Cost


class CostTypeFilter(filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='contains')

    class Meta:
        model = CostType
        fields = ['name']


class UnitFilter(filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='contains')

    class Meta:
        model = Unit
        fields = ['name']


class CostFilter(filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='contains')
    costtype = CharFilter(field_name='costtype__name', lookup_expr='contains')
    buy_time = DateTimeFromToRangeFilter(field_name='buy_time')
    price = RangeFilter(field_name='_price')

    class Meta:
        model = Cost
        fields = ['name', 'costtype', 'buy_time', '_price']
