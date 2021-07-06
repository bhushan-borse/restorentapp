from flask import Flask
from database.connect_to_mongo import init_mongo_db
from routes.register_route import register_route
app = Flask(__name__)

app.config['MONGO_URI'] ="mongodb+srv://restorent-app:2GUVjVbpJNUhgKq@cluster0.1dz4v.mongodb.net/restorent?retryWrites=true&w=majority"

PACKGES = [
    "tabel_management"
]

app.url_map.strict_slashes = False

init_mongo_db(app=app)
register_route(app=app, packages=PACKGES)
if __name__ == '__main__':
    app.run(debug=True, host="localhost", port="9000")