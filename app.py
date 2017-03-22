"""Script to crawl Top Posts across sub reddits and store results in MongoDB
"""

from scrapy.crawler import CrawlerProcess
from reddit.spiders import PostSpider

if __name__ == '__main__':
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(PostSpider)
    process.start() # the script will block here until the crawling is finished
