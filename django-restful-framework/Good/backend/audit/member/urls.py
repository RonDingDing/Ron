from django.urls import path
from rest_framework import routers

from audit.member.views import MemberViewSet, CouponViewSet, MemberPlanViewSet, CouponItemViewSet

router = routers.SimpleRouter()
router.register(r'member', MemberViewSet)
router.register(r'coupon', CouponViewSet)
router.register(r'couponitem', CouponItemViewSet)
urlpatterns = router.urls  + [
    path('', MemberPlanViewSet.as_view({'get': 'list'}))
]

