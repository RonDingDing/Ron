from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ModelViewSet

from .filterclass import MemberFilter, CouponItemFilter, CouponFilter
from .serializers import CouponCreateSerializer, CouponListRetrieveSerializer, CouponUpdateSerializer
from .serializers import MemberSerializer, CouponItemSerializer
from ..baseviewset import NoDeleteNoModifyModelViewSet
from ..models import Member, Coupon, CouponItem


class MemberViewSet(NoDeleteNoModifyModelViewSet):
    queryset = Member.objects.order_by('name')
    serializer_class = MemberSerializer
    filter_class = MemberFilter


    def perform_create(self, serializer):
        serializer.Meta.model.objects.get_or_create(**serializer.validated_data)


class CouponViewSet(ModelViewSet):
    queryset = Coupon.objects.order_by('user__id')
    filter_class = CouponFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return CouponCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return CouponUpdateSerializer
        return CouponListRetrieveSerializer

    def perform_create(self, serializer):
        user = serializer.validated_data['user']
        user_coupon = serializer.Meta.model.objects.filter(user=user)
        if user_coupon:
            user_coupon.update(**serializer.validated_data)
        else:
            serializer.save()


class CouponItemViewSet(NoDeleteNoModifyModelViewSet):
    queryset = CouponItem.objects.order_by('id')
    serializer_class = CouponItemSerializer
    filter_class = CouponItemFilter

    def perform_create(self, serializer):
        serializer.Meta.model.objects.get_or_create(**serializer.validated_data)


class MemberPlanViewSet(GenericViewSet):
    def list(self, request, *args, **kwargs):
        return Response({
            '会员': str(request._request._current_scheme_host) + '/member/member/',
            '优惠券': str(request._request._current_scheme_host) + '/member/coupon/',
            '优惠券种类': str(request._request._current_scheme_host) + '/member/couponitem/',

        })
