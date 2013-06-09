# -*- coding: utf-8 -*-

import os

import flask as f
from flask import Flask,session
#import flask.ext.assets as fassets

import config.conf as conf

from model import BasicUser

app = Flask(__name__)

app.config.from_object("conure.config.conf")
#assets = fassets.Environment(app)
#assets.versions = 'hash:32'

@app.before_request
def something_before_request():
    if "user" not in session:
        user            = BasicUser.get_user_by_nickname("guest")
        session["user"] = user.to_dict()


import controllers

from util.filter import timesince
app.jinja_env.filters['timesince']  = timesince
