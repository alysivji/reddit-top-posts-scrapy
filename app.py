"""Script to crawl Top Posts across sub reddits and store results in MongoDB
"""

from scrapy.crawler import CrawlerProcess
from reddit.spiders import PostSpider
from scrapy.utils.project import get_project_settings
from top_post_emailer import email_last_scraped_date

if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())

    process.crawl(PostSpider)
    process.start() # the script will block here until the crawling is finished

    email_last_scraped_date()
