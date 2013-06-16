from flask import request,session,jsonify,render_template

from conure.application import app
from conure.model import Feed,FeedSite,ReadFeed,Sub



@app.route("/api/feed/<feedid>",methods=["PUT"])
def update_feed(feedid):
    feed          = Feed.get_feed_by_id(feedid)
    unread        = request.json.get("unread",None)
    if unread == False:
        session["user"].read_feed(feed)
    else:
        session["user"].unread_feed(feed)


    return jsonify(rcode=200)