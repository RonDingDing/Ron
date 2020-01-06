from audit.management.views import CostTypeViewSet, ProducttypeViewSet, ProductViewSet, UnitViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'unit', UnitViewSet)
router.register(r'costtype', CostTypeViewSet)
router.register(r'producttype', ProducttypeViewSet)
router.register(r'product', ProductViewSet)
urlpatterns = router.urls

