from flask import request
from flask.views import MethodView
from config.config_class import ViewConfig
from response.response import create_response


class BaseClass(MethodView):

    def __init__(self, view_config: ViewConfig):
        self.view_config: ViewConfig = view_config

    def get(self, **kwargs):
        field = self.view_config.get_obj_key
        get_obj_key = request.args.get(field)
        if get_obj_key:
            return create_response(
                data=self.view_config.model.objects.filter(**{field: get_obj_key}).first(),
                message="Success!."
            )
        return create_response(
            data=self.view_config.model.objects().all(),
            message="Success!."
        )

    def post(self):
        req_data = request.get_json()
        obj = self.view_config.model(**req_data)
        try:
            obj.save()
            return create_response(message="Data Successfully Save!..")
        except Exception as error:
            import traceback
            print(traceback.format_exc())
            return create_response(error="Something Went Wrong!...")

    def delete(self, **kwargs):
        field = self.view_config.get_obj_key
        get_obj_key = request.args.get(field)
        if get_obj_key:
            query = self.view_config.model.objects.filter(**{field: get_obj_key})
            if query:
                query.delete()
                return create_response(
                    message="Success!."
                )
            return create_response(
                message="No data Found!."
            )
        return create_response(
            data=self.view_config.model.objects().all(),
            message=f"Please Send the {field} data!."
        )

    def put(self, **kwargs):
        field = self.view_config.get_obj_key
        get_obj_key = request.args.get(field)
        if get_obj_key:
            query = self.view_config.model.objects.filter(**{field: get_obj_key})
            if query:
                query.update(**request.get_json())
                return create_response(
                    message="Success!."
                )
            return create_response(
                message="No data Found!."
            )
        return create_response(
            data=self.view_config.model.objects().all(),
            message=f"Please Send the {field} data!."
        )
