﻿# -*- coding: utf-8 -*-

import os

import flask as f
from flask import Flask
#import flask.ext.assets as fassets

import config.conf as conf


app = Flask(__name__)

app.config.from_object("conure.config.conf")
#assets = fassets.Environment(app)
#assets.versions = 'hash:32'

@app.before_request
def something_before_request():
    pass


import controllers

from util.filter import timesince
app.jinja_env.filters['timesince']  = timesince
