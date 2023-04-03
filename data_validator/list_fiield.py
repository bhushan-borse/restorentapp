from data_validator import field_abs
from data_validator import constant


class ListField(field_abs.Field):

    def validate(self):
        try:
            if not isinstance(self.value, list):
                self.is_valid = False
                self.error_message = constant.ErrorMessages.LIST_FAIL.value.format(
                    self.field_name, self.value
                )
        except:
            self.is_valid = False
            self.error_message = constant.ErrorMessages.LIST_FAIL.value.format(
                self.field_name, self.value
            )
