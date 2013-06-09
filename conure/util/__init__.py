# -*- coding: utf-8 -*-


def time_struct_to_datetime(dt):
    from datetime import datetime
    from time import mktime
    return datetime.fromtimestamp(mktime(dt))