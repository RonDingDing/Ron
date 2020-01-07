from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
class PlanViewSet(GenericViewSet):
    def list(self, request, *args, **kwargs):
        return Response({
            '收入': str(request._request._current_scheme_host) + '/revenue/',
            '支出': str(request._request._current_scheme_host) + '/cost/',
            '会员': str(request._request._current_scheme_host) + '/member/',
        })