# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from reddit.items import RedditItem
from datetime import datetime

class PostSpider(scrapy.Spider):
    name = 'post'
    allowed_domains = ['reddit.com']

    reddit_urls = [
        ('datascience', 'week'),
        ('python', 'week'),
        ('programming', 'week'),
    ]

    #period = 'week'
    start_urls = ['https://www.reddit.com/r/' + sub + '/top/?sort=top&t=' + period \
        for sub, period in reddit_urls]

    def parse(self, response):
        # get the subreddit from the URL
        sub = response.url.split('/')[4]

        # parse thru each of the posts
        for post in response.css('div.thing'):
            item = RedditItem()

            item['date'] = datetime.today()
            item['sub'] = sub
            item['title'] = post.css('a.title::text').extract_first()
            item['url'] = post.css('a.title::attr(href)').extract_first()
            item['score'] = post.css('div.unvoted::text').extract_first()
            item['commentsUrl'] = post.css('a.comments::attr(href)').extract_first()

            yield item
