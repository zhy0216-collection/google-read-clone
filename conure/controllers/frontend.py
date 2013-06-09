# -*- coding: utf-8 *-*
from collections import Counter

from flask import url_for, \
    redirect, g, flash, request, current_app,\
    render_template, session,jsonify, abort

from conure.application import app
from conure.model import Feed,FeedSite


@app.route("/")
def main():
    sites       = FeedSite.objects()

    return render_template( 'main.html',sites=sites)
@app.route("/fav_icon")
def site_fav():
    site_link   = request.args.get("site_link",None)
    pass








