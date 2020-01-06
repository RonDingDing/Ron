from audit.cost.views import CostViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'', CostViewSet)
urlpatterns = router.urls