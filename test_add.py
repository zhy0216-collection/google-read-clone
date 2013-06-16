


from conure.model.feed import Feed,FeedSite








if __name__ == "__main__":
    test_url        = 'http://feed.williamlong.info/'
    FeedSite.add_from_feed_url(test_url, parse_immediately=True)








