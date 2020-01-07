from audit.revenue.views import  RevenueViewSet, ProducttypeViewSet, ProductViewSet, ProductPlanViewSet
from rest_framework import routers
from django.urls import path
router = routers.SimpleRouter()
router.register(r'revenue',  RevenueViewSet)
router.register(r'producttype', ProducttypeViewSet)
router.register(r'product', ProductViewSet)
urlpatterns = router.urls + [
    path('', ProductPlanViewSet.as_view({'get': 'list'}))
]




