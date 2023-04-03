from data_validator import schema
from data_validator import int_field
from data_validator import float_field


class Student(schema.Schema):
    s_int_id = int_field.IntField()
    s_float_id = float_field.FloatField()
