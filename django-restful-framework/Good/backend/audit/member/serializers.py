from ..baseserializer import DynamicFieldsModelSerializer
from ..models import Member, Coupon

class MemberSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class CouponListRetrieveSerializer(DynamicFieldsModelSerializer):
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