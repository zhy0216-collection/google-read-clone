# coding:utf8

from flask.ext.mongoengine import MongoEngine

from conure.config import config as conf

def get_db(database=None):
    if not database:
        database = conf.MONGODB_DB
    if conf.TESTING:
        database = conf.MONGODB_DB_UNITTEST
    mongo = MongoEngine()
    mongo.connect(
        database,
        host=conf.MONGODB_HOST,
        port=conf.MONGODB_PORT,
        username=conf.MONGODB_USER,
        password=conf.MONGODB_PASSWD
    )
    return mongo

db = get_db()