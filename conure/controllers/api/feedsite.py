from flask import request,session,jsonify,render_template

from conure.application import app
from conure.model import FeedSite



@app.route("/api/feedsite/",methods=["POST"])
def add_feedsite():
    feed_url    = request.form.get("feed_url",None)

    site        = session["user"].add_feed(feed_url)
    return jsonify(rcode=200)

@app.route("/feedsite/<siteid>",methods=["GET"])
def show_feedsite(siteid):
    fs  = FeedSite.get_feed_items_by_siteid(siteid)
    return render_template("feedsite.html",feedsite=fs)










