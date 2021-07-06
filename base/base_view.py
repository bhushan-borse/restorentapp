from flask import jsonify, request
from flask.views import MethodView
from response.response import  success_response, error_response
class BaseClass(MethodView):
    model = None
    select_list_fields = []
    select_dict_fields = []
    pk_fiels = "_id"
    
    def get_obj(self, obj):
        select_dict_fields = self.select_dict_fields or self.select_list_fields
        return {field: getattr(obj, field, None) for field in select_dict_fields}
    
    def get_objects(self, objects):
        return [{ {field: getattr(obj, field, None) for field in self.select_list_fields} } for obj in objects]

    def get(self, **kwargs):
        pk = kwargs.get(self.pk_fiels)
        if pk:
            return jsonify(self.get_obj({}))
        else:
            return jsonify(self.get_pagination_data())
    
    def post(self):
        req_data = request.get_json()
        obj = self.model(**req_data)
        try:
            obj.save()
            response = success_response(message="Data Successfully Save!..")
        except Exception as error:
            response = error_response(error="Something Went Wrong!...")
        return jsonify(response)
    
    