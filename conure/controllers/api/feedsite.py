from flask import request,session,jsonify

from conure.application import app




@app.route("/api/feedsite/",methods=["POST"])
def add_feedsite():
    feed_url    = request.form.get("feed_url",None)
    
    site        = session["user"].add_feed(feed_url)
    return jsonify(rcode=200)





