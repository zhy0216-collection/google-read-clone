# -*- coding: utf-8 *-*

import string,random
import hashlib
from datetime import datetime as dt

from conure.libs.db import db
from .feed import FeedSite,Feed

class Validator(object):
    email       = db.StringField(required=True)
    password    = db.StringField(required=True)

    @classmethod
    def is_valid(cls,email,password):
        user = cls.objects(email=email,password=password).first()
        return user is not None

    @classmethod
    def validate_user(cls, email, password):
        return cls.objects(email=email,password=password).first()

class User(Validator):
    info            = db.EmbeddedDocumentField("UserInfo")
    setting         = db.EmbeddedDocumentField("UserSetting")
    default_folder  = db.ReferenceField("FeedFolder")
    type            = "user"


    @property
    def nickname(self):
        return self.info.nickname

    @classmethod
    def get_user_by_id(cls,id):
        return cls.objects(id=id).first()

    @classmethod
    def get_user_by_nickname(cls,nickname):
        return cls.objects(info__nickname=nickname).first()

    #
    def has_feedsite(self,feedsite):
        from user_feed import Sub
        return Sub.exist_sub(self.id,feedsite)

    def read_feed(self,feed):
        from user_feed import ReadFeed,Sub
        rf  = ReadFeed.get_readfeed_by_feed_and_userid(feed=feed,
                                        userid=self.id)
        if rf.unread:
            sub  = Sub.get_sub_by_userid_feedsite(userid=self.id,feedsite=feed.feedsite)
            sub.unread_counter -=1
            sub.save()
        rf.unread = False
        rf.safe_save()


    def unread_feed(self,feed):
        pass

    def has_read(self,feed=None):
        from user_feed import ReadFeed
        rf  = ReadFeed.get_readfeed_by_feed_and_userid(feed=feed,userid=self.id)
        return not rf.unread

    def add_feed(self,feed_url):
        from user_feed import Sub
        from feed import FeedSite

        fs = FeedSite.get_from_feed_url(feed_url)
        if self.has_feedsite(fs):
            return None
        fs  = FeedSite.add_from_feed_url(feed_url,parse_immediately =True)
        self.default_folder.site_list.append(fs)
        self.default_folder.save()
        Sub.add_sub(self.id,fs)

        return fs
    #
    def create_folder(self,folder_name):
        from user_feed import FeedFolder
        ff          = FeedFolder(name=folder_name)
        ff.userid   = self.id
        ff.safe_save()
        return ff

    def get_all_folders(self):
        from user_feed import FeedFolder
        return FeedFolder.get_folders_by_userid(self.id)

    @property
    def all_folders(self):
        return self.get_all_folders()

    def get_unread_feeds_on_feedsite(self,feedsite):
        from user_feed import Sub
        counter  = Sub.get_unread_counter_by_userid_feedsite(userid=self.id,
                                                            feedsite=feedsite)
        return counter

    def to_dict(self):
        return {"id":str(self.id),
                "nickname":self.info.nickname,
                "type":self.type
        }

class UserInfo(db.EmbeddedDocument):
    nickname    = db.StringField(required=True)


class UserSetting(db.EmbeddedDocument):
    theme       = db.StringField(default="google")


class BasicUser(db.Document,User):
    type        = "basic"


    def upgrade(self):
        pass

    def subscribe(self,site):
        pass

class AdvancedUser(db.Document,User):
    pass

#help other class to access user attributes
class UserAccesser(object):
    userid      = db.ObjectIdField() # consider two type of user

    @property
    def user(self):
        return BasicUser.get_user_by_id(self.userid) \
               or  AdvancedUser.get_user_by_id(self.userid)





