from base.base_view import BaseClass
from tabel_management.models import TableManagement
from config.config_class import RouteConfig, ViewConfig


class TableManagementView(BaseClass):
    pass


def get_api_view():
    '''
    config the Router will register these to app router
     '''
    view_list = [
        RouteConfig(
            view_class=TableManagementView,
            url="/table",
            view_config=ViewConfig(
                model=TableManagement,
                get_obj_key="tabel_management_id"
            ),
            methods=['GET', 'POST', 'PUT', 'DELETE'],

        )
    ]
    return view_list
