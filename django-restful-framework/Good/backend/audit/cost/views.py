from ..models import Cost
from .serializers import CostListRetrieveSerializer, CostCreateSerializer

from restframework_datachange.viewsets import RModelViewSet

class CostViewSet(RModelViewSet):
    queryset = Cost.objects.all()
    def get_serializer_class(self):
        if self.action == 'create':
            return CostCreateSerializer
        return CostListRetrieveSerializer

    def perform_create(self, serializer):
        serializer.Meta.model.objects.get_or_create(**serializer.validated_data)