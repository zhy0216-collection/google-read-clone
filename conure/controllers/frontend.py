# -*- coding: utf-8 *-*
from collections import Counter

from flask import url_for, \
    redirect, g, flash, request, current_app,\
    render_template, session,jsonify, abort

from conure.application import app


@app.route("/")
def main():
    return render_template( 'main.html')










