from audit.revenue.views import  RevenueViewSet
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'',  RevenueViewSet)
urlpatterns = router.urls


