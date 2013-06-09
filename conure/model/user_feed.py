

# user <-> sites
class Sub(object):
    pass

# user <-> folder <- sites <- feed
# for only for view, ignore at first
class FeedFolder(object):
    pass


#user <-> feeds, means use start a feed;
#it is possible that user can star a feed but have not read it
class StarFeed(object):
    pass


#user <-> feeds, means user has read the feed
class ReadFeed(object):
    pass


