from data_validator import field_abs
from data_validator import constant


class DictField(field_abs.Field):

    def validate(self):
        try:
            if not isinstance(self.value, dict):
                self.is_valid = False
                self.error_message = constant.ErrorMessages.DICT_FAIL.value.format(
                    self.field_name, self.value
                )
        except:
            self.is_valid = False
            self.error_message = constant.ErrorMessages.DICT_FAIL.value.format(
                self.field_name, self.value
            )
