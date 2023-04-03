from data_validator import field_abs
from data_validator import constant


class IntField(field_abs.Field):
    def validate(self):
        try:
            self.validated_value = int(eval(str(self.value)))
        except:
            self.is_valid = False
            self.error_message = constant.ErrorMessages.INT_FAIL.value.format(
                self.field_name, self.value
            )
