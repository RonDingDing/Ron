from ..baseserializer import DynamicFieldsModelSerializer
from ..models import Member

class MemberSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
