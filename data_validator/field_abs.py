from data_validator import constant


class Field(object):
    def __init__(
            self, allow_null=True, allow_blank=True, default_value=None,
            is_required=False, field_name=None, *args, **kwargs
    ):

        self.default_value = default_value
        self.value = None
        self.is_valid = True
        self.allow_null = allow_null
        self.allow_blank = allow_blank
        self.is_required = is_required
        self.error_message = ""
        self.field_name = field_name
        self.validated_value = None

    def __call__(self, value):
        if self.default_value and not value:
            if callable(self.default_value):
                self.value = self.default_value()
                return
            self.value = self.default_value
            return
        self.value = value

    def check_common_validator(self):

        if self.is_required and not self.value:
            self.is_valid = False
            self.error_message = constant.ErrorMessages.REQUIRE.value.format(self.field_name)
            return False

        if self.allow_blank and self.value == "":
            self.is_valid = False
            self.error_message = constant.ErrorMessages.AL_BLANK.value.format(self.field_name)
            return False

        if self.allow_null and self.value is None:
            self.is_valid = False
            self.error_message = constant.ErrorMessages.AL_NULL.value.format(self.field_name)
            return False

        return True

    def __repr__(self):
        return f"{self.field_name}={self.value}"
