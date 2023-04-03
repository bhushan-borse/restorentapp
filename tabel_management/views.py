from base.base_view import BaseClass
from tabel_management.models import TableManagement
from config.config_class import RouteConfig, ViewConfig


class View(BaseClass):
    pass


def get_api_view():
    view_list = [
        RouteConfig(
            view_class=View,
            url="/table",
            view_config=ViewConfig(
                model=TableManagement
            ),
            methods=['GET', 'POST', 'PUT', 'DELETE']
        )
    ]
    return view_list
