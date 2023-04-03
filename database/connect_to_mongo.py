from flask_mongoengine import MongoEngine

db = MongoEngine()


def init_mongo_db(app):
    db.init_app(app)
