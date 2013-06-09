# -*- coding: utf-8 -*-









class Feed(object):
    pass


class FeedSite(object):
    url             = db.StringField()
    name            = db.StringField()
    icon_image      = db.StringField()#url


    @property
    def domain(self):
        pass




















