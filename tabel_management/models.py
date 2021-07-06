from database.connect_to_mongo import db
from base.common_fun import get_uuid

class TabelManagement(db.Document):
    tabel_management_id = db.StringField(required=True, primary_key=True, default=get_uuid)
    tabel_code = db.StringField(required=True)
    
    
    meta = {'collection': 'tabel_management'}
