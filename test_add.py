


from conure.model.feed import Feed,FeedSite








if __name__ == "__main__":
    test_url        = 'http://solidot.org.feedsportal.com/c/33236/f/556826/index.rss'
    FeedSite.add_from_feed_url(test_url, parse_immediately=True)
    
    






