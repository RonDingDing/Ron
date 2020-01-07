from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import MemberSerializer
from ..baseviewset import NoDeleteNoModifyModelViewSet
from ..models import Member


class MemberViewSet(NoDeleteNoModifyModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def perform_create(self, serializer):
        serializer.Meta.model.objects.get_or_create(**serializer.validated_data)


CouponViewSet = MemberViewSet


class MemberPlanViewSet(GenericViewSet):
    def list(self, request, *args, **kwargs):
        return Response({
            '会员': str(request._request._current_scheme_host) + '/member/member/',
            '优惠券': str(request._request._current_scheme_host) + '/member/coupon/',

        })
