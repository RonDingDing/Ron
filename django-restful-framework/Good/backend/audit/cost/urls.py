from audit.cost.views import CostViewSet, CostTypeViewSet, CostPlanViewSet, UnitViewSet
from rest_framework import routers
from django.urls import path

router = routers.SimpleRouter()
router.register(r'cost', CostViewSet)
router.register(r'costtype', CostTypeViewSet)
router.register(r'unit', UnitViewSet)
urlpatterns = router.urls + [
    path('', CostPlanViewSet.as_view({'get':'list'}))
]