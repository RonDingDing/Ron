from django_filters import rest_framework as filters, CharFilter

from ..models import Member, CouponItem, Coupon


class MemberFilter(filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='contains')
    phone = CharFilter(field_name='phone', lookup_expr='contains')

    class Meta:
        model = Member
        fields = ['name', 'phone']


class CouponItemFilter(filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='contains')

    class Meta:
        model = CouponItem
        fields = ['name']

class CouponFilter(filters.FilterSet):
    user = CharFilter(field_name='user__name', lookup_expr='contains')

    class Meta:
        model = Coupon
        fields = ['user']
