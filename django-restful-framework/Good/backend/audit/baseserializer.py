from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError

class DynamicFieldsModelSerializer(ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


    def is_valid(self, raise_exception=False):
        assert not hasattr(self, 'restore_object'), (
                'Serializer `%s.%s` has old-style version 2 `.restore_object()` '
                'that is no longer compatible with REST framework 3. '
                'Use the new-style `.create()` and `.update()` methods instead.' %
                (self.__class__.__module__, self.__class__.__name__)
        )

        assert hasattr(self, 'initial_data'), (
            'Cannot call `.is_valid()` as no `data=` keyword argument was '
            'passed when instantiating the serializer instance.'
        )

        if not hasattr(self, '_validated_data'):
            try:
                self._validated_data = self.run_validation(self.initial_data)
            except ValidationError as exc:
                self._validated_data = {}
                self._errors = exc.detail
            else:
                self._errors = {}

        # 覆盖源码的 is_valid 方法，以上均复制源码，只改了下面这句，使多个错误字段变成detail字段
        if self._errors and raise_exception:
            if isinstance(self.errors, dict):
                a, b = list(self.errors.items())[0]
                raise ValidationError({'msg': a + '：' + b[0]})

        return not bool(self._errors)
