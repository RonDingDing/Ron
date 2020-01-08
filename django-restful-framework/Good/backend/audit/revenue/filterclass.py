from django_filters import rest_framework as filters, CharFilter, DateTimeFromToRangeFilter

from ..models import Product, ProductType, Order


class ProductFilter(filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='contains')

    class Meta:
        model = Product
        fields = ['name', ]


class ProductTypeFilter(filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='contains')

    class Meta:
        model = ProductType
        fields = ['name', ]


class OrderFilter(filters.FilterSet):
    member = CharFilter(field_name='member__name', lookup_expr='contains')
    sale_time = DateTimeFromToRangeFilter(field_name='sale_time')


    class Meta:
        model = Order
        fields = ['sale_time', 'member']
