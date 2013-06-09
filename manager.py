# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

from flask.ext.script import Manager

from ezlog2 import app



@manager.command
def clean_db():
    from pymongo import MongoClient
    conn = MongoClient(config.MONGODB_HOST, config.MONGODB_PORT)
    conn.drop_database(config.MONGODB_DB)
    conn.close()