"""Script to crawl Top Posts across sub reddits and store results in MongoDB
"""

import logging
from datetime import date
from scrapy.crawler import CrawlerProcess
from reddit.spiders import PostSpider
from scrapy.utils.project import get_project_settings
from top_post_emailer import email_last_scraped_date

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # only run on saturdays (once a week)
    if date.strftime(date.today(), '%A').lower() == 'friday':
        crawler = CrawlerProcess(get_project_settings())

        crawler.crawl(PostSpider)
        crawler.start() # the script will block here until the crawling is finished

        email_last_scraped_date()
        logger.info('Scrape complete and email sent.')
    else:
        logger.info('Script did not run.')
