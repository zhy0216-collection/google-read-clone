

from conure.libs.db import db
from .user import UserAccesser



# user <-> sites
class Sub(db.Document,UserAccesser):
    feedsite        = db.ReferenceField("FeedSite")
    counter         = db.IntField(default=0)
    unread_counter  = db.IntField(default=0)

    meta = {
        'allow_inheritance': False,
        'index_types': False,
        'indexes': [
            {'fields': ['userid','feedsite'],'unique': True},
        ]
    }
    
    @classmethod
    def add_sub(cls,userid,feedsite):
        self.userid     = userid
        self.feedsite   = feedsite
        self.save()
        return self


# all user sub subscript is in uncategoried folder

# user <-> folder <- sites <- feed
# for only for view, ignore at first
class FeedFolder(db.Document,UserAccesser):
    name        = db.StringField(required=True)
    site_list   = db.ListField(db.ReferenceField("FeedSite"))
    has_open    = db.BooleanField(default=False)

    meta = {
        'allow_inheritance': False,
        'index_types': False,
        'indexes': [
            {'fields': ['userid']},
        ]
    }

    @classmethod
    def get_folders_by_userid(cls,userid):
        return cls.objects(userid=userid)

    def safe_save(self):
        self.save()

    def safe_delete(self):
        self.delete()

    @property
    def unread_feeds(self):
        pass

    @property
    def unread_feeds_counter(self):
        #100+ not 1000+
        sum_counter     = 0
        for fs in self.site_list:
            t   = fs.get_unread_feeds_counter_by_userid(userid)
            fs.unread_feeds_counter = t
            sum_counter += t
        return sum_counter if sum_counter <= 100 else "100+"


#user <-> feeds, means use start a feed;
#it is possible that user can star a feed but have not read it
class StarFeed(db.Document,UserAccesser):
    pass


#user <-> feeds, means user has read the feed
class ReadFeed(db.Document,UserAccesser):
    pass


