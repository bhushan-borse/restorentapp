from data_validator import field_abs


class Schema(object):
    def __init__(self, data=None, is_bulk=False):
        self.data = data
        self.is_bulk = is_bulk
        self.fields = []

    def serialize_data(self):
        pass

    def validate(self):
        self_dir = dir(self)
        for s_dir in self_dir:
            field = getattr(self, s_dir, None)

            if isinstance(field, field_abs.Field):

                self.fields.append({
                    "field": field,
                    "field_name": s_dir
                })

        print(f"{self_dir=}, {self.fields}")
