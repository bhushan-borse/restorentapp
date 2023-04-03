import importlib
from flask import Flask
from config.config_class import RouteConfig


def hello():
    return {"hello": "hello"}


def register_route(app: Flask = None, packages: list = None):
    app.add_url_rule("/hello", view_func=hello, methods=["GET"])

    if not packages:
        return None

    if not app:
        return None

    def reg_route(view_conf_obj: RouteConfig):
        view_func = view_conf_obj.view_class.as_view(view_conf_obj.endpoint, view_conf_obj.view_config)
        app.add_url_rule(view_conf_obj.url, view_func=view_func, methods=view_conf_obj.methods)

    for package in packages:
        try:
            module = importlib.import_module(f"{package}.views")
            view_list = module.get_api_view()
            for view_obj in view_list:
                reg_route(view_obj)
        except Exception as err:
            import traceback
            print("[ERROR] Route Registration:- ", traceback.format_exc())
            return err
