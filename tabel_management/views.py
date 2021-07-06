
from base.base_view import BaseClass
from tabel_management.models import TabelManagement

class TabelManagementAPIView(BaseClass):
    select_list_fields = ["tabel_id"]
    select_dict_fields = ["tabel_id"]
    model = TabelManagement

def get_api_view():
    
    view_list = [
        {
            "view_class": TabelManagementAPIView,
            "url": "/tabel",
            "pk" : "_id",
            "pk_type": "string",
            "endpoint": "tabel"
        }
    ]
    return view_list