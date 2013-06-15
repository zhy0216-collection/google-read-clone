from flask import request,session,jsonify,render_template

from conure.application import app
from conure.model import Feed,FeedSite



@app.route("/api/feedsite/",methods=["POST"])
def add_feedsite():
    feed_url    = request.form.get("feed_url",None)
    site        = session["user"].add_feed(feed_url)
    return jsonify(rcode=200)

@app.route("/feedsite/<siteid>",methods=["GET"])
def show_feedsite(siteid):
    #feeds  = Feed.get_feed_items_by_siteid(siteid)
    return render_template("feedsite.html")

@app.route("/api/feedsite/<siteid>",methods=["GET"])
def show_feedsite_api(siteid):
    feeds  = Feed.get_feed_items_by_siteid(siteid)
    return render_template("feedsite.html",
                            feeds=feeds,
                            API = True)
    









