from data_validator import IntField, FloatField, Schema


class Student(Schema):
    s_int_id = IntField()
    s_float_id = FloatField()


data = [
    {
        "s_int_id": "asd",
        "s_float_id": 10.5,
    }
]

data = Student(data, is_bulk=True)

data.validate()

print(data)
