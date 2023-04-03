from flask import Flask
from routes.register_route import register_route
from database.connect_to_mongo import init_mongo_db

app = Flask(__name__)

# app.config['MONGO_URI'] = "mongodb+srv://localhost:27012/restorent"

app.config["MONGODB_SETTINGS"] = [
    {
        "db": "restorent",
        "host": "localhost",
        "port": 27017
    }
]

PACKGES = [
    "tabel_management"
]

app.url_map.strict_slashes = False

init_mongo_db(app=app)
register_route(app=app, packages=PACKGES)

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=9000)
