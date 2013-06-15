# -*- coding: utf-8 -*-


import feedparser

from conure.libs.db import db
from conure.util import time_struct_to_datetime

class Feed(db.Document):
    title               = db.StringField(required=True, default="No title")
    link                = db.StringField()
    content             = db.StringField()
    summary             = db.StringField()
    create_date         = db.DateTimeField() #

    feedsite            = db.ReferenceField("FeedSite")

    meta = {
        'allow_inheritance': False,
        'index_types': False,
        'ordering': ['-create_date']
    }

    def is_newer_than(self,tdate):
        pass


class FeedSite(db.Document):
    feed_url            = db.StringField(required=True) # the user input
    site_link           = db.StringField() # we calculate it
    title               = db.StringField()
    fav_icon            = db.StringField() # url->need site_link
    last_pub_time       = db.DateTimeField() #the last feeditem's time

    feed_items          = db.SortedListField(db.ReferenceField("Feed"),
                                             ordering="-create_date")

    meta = {
        'allow_inheritance': False,
        'index_types': False,
        'indexes': [
            {'fields': ['feed_url'], 'unique': True},
        ]
    }

    @classmethod
    def get_feed_items_by_siteid(cls,siteid):
        return cls.objects(id=siteid).only("feed_items").first()

    @classmethod
    def add_from_feed_url(cls,feed_url,parse_immediately=False):
        site    = cls.get_from_feed_url(feed_url) or cls(feed_url=feed_url)
        if parse_immediately:
            if site.id:
                site.refresh()
            else:
                site._parse()
        else:
            pass #send a message to rabbitmq

        return site.save() # need to try-catch?

    @classmethod
    def get_from_feed_url(cls,feed_url):
        return cls.objects(feed_url=feed_url).first()

    def refresh(self):
        print "refresh"

    # only use when the site get feed_url
    # to create feedsite object
    def _parse(self):
        d = feedparser.parse(self.feed_url)
        self.title          = d.feed.title
        self.site_link      = d.feed.link
        self.last_pub_time  = time_struct_to_datetime(d.feed.updated_parsed)
        #to get fav_icon

        #parse the feeditem
        for entry in d.entries[::-1]:
            feed                = Feed(title=entry.title)
            feed.link           = entry.link
            feed.content        = entry.description
            feed.summary        = entry.summary
            feed.create_date    = time_struct_to_datetime(entry.published_parsed)
            feed.feedsite       = self
            feed.save()
            self.feed_items.append(feed)

    @property
    def feed_item_counter(self):
        return len(self.feed_items)

    @property
    def domain(self):
        pass




















