from audit.member.views import MemberViewSet, CouponViewSet, MemberPlanViewSet
from rest_framework import routers
from django.urls import path

router = routers.SimpleRouter()
router.register(r'member', MemberViewSet)
router.register(r'coupon', CouponViewSet)

urlpatterns = router.urls  + [
    path('', MemberPlanViewSet.as_view({'get': 'list'}))
]

