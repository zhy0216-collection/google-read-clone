from flask import request,session,jsonify,render_template

from conure.application import app
from conure.model import Feed,FeedSite,ReadFeed



@app.route("/api/feed/<feedid>",methods=["PUT"])
def update_feed(feedid):
    feed          = Feed.get_feed_by_id(feedid)
    unread        = request.json.get("unread",None)
    if unread is not None:
        rf        = ReadFeed.get_readfeed_by_feed_and_userid(feed=feed,
                                                             userid=session["user"].id)
        rf.unread = unread
        rf.safe_save()

    return jsonify(rcode=200)