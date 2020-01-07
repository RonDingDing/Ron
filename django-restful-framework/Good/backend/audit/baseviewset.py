from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

class NoDeleteNoModifyModelViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet):
    pass