# -*- coding: utf-8 *-*

import string,random
import hashlib
from datetime import datetime as dt

from conure.libs.db import db

class Validator(object):
    email       = db.StringField(required = True)
    password    = db.StringField(required = True)

    @classmethod
    def is_valid(cls,email,password):
        user = cls.objects(email=email,password=password).first()
        return user is not None

    @classmethod
    def validate_user(cls, email, password):
        return cls.objects(email=email,password=password).first()

class User(Validator):
    setting     = db.ReferenceField("UserSetting")

class UserSetting(object):
    pass

class BasicUser(db.Document,User):
    type        = "basic"

    def subscribe(self,site):
        pass

class AdvancedUser(db.Document,User):
    pass






