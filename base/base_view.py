from flask import request
from flask.views import MethodView
from config.config_class import ViewConfig
from response.response import create_response


class BaseClass(MethodView):

    def __init__(self, view_config: ViewConfig):
        self.view_config: ViewConfig = view_config

    def get(self, **kwargs):
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
