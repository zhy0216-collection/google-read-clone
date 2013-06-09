# -*- coding: utf-8 *-*

import string,random
import hashlib
from datetime import datetime as dt

from conure.libs.db import db

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
    info        = db.EmbeddedDocumentField("UserInfo")
    setting     = db.ReferenceField("UserSetting")
    type        = "user"

    @classmethod
    def get_user_by_id(cls,id):
        return cls.objects(id=id).first()
        
    @classmethod
    def get_user_by_nickname(cls,nickname):
        return cls.objects(info__nickname=nickname).first()

    def get_unread_feeds(self):
        pass

    def to_dict(self):
        return {"id":str(self.id),
                "nickname":self.info.nickname,
                "type":self.type
        }

class UserInfo(db.EmbeddedDocument):
    nickname    = db.StringField(required=True)


class UserSetting(db.Document):
    theme       = db.StringField(default="google")


class BasicUser(db.Document,User):
    type        = "basic"

    def subscribe(self,site):
        pass

class AdvancedUser(db.Document,User):
    pass






