from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import MemberSerializer
from ..baseviewset import NoDeleteNoModifyModelViewSet
from ..models import Member, Coupon
from rest_framework.viewsets import ModelViewSet
from .serializers import CouponCreateSerializer, CouponListRetrieveSerializer, CouponUpdateSerializer


class MemberViewSet(NoDeleteNoModifyModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def perform_create(self, serializer):
        serializer.Meta.model.objects.get_or_create(**serializer.validated_data)


class CouponViewSet(ModelViewSet):
    queryset = Coupon.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CouponCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return CouponUpdateSerializer
        return CouponListRetrieveSerializer


class MemberPlanViewSet(GenericViewSet):
    def list(self, request, *args, **kwargs):
        return Response({
            '会员': str(request._request._current_scheme_host) + '/member/member/',
            '优惠券': str(request._request._current_scheme_host) + '/member/coupon/',

        })
