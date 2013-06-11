

from conure.libs.db import db
from .user import UserAccesser



# user <-> sites
# class Sub(object):
    # pass
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
        return 0


#user <-> feeds, means use start a feed;
#it is possible that user can star a feed but have not read it
class StarFeed(db.Document,UserAccesser):
    pass


#user <-> feeds, means user has read the feed
class ReadFeed(db.Document,UserAccesser):
    pass


