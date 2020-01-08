from rest_framework.serializers import SlugRelatedField

from ..baseserializer import DynamicFieldsModelSerializer
from ..models import Member, Coupon, CouponItem


class MemberSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class CouponListRetrieveSerializer(DynamicFieldsModelSerializer):
    user = SlugRelatedField(slug_field='name', read_only=True)
    coupon = SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Coupon
        fields = '__all__'


class CouponCreateSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'


class CouponUpdateSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'


class CouponItemSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = CouponItem
        fields = '__all__'
