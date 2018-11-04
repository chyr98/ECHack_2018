from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import CrawlSpider, Rule, Spider
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from theonionscraper.items import TheOnionScraperItem
DOMAIN = 'theonion.com'
URL = 'http://%s' % DOMAIN
class OnionDataSpider(Spider):
    name = "onion_data_spider"
    allowed_domains = [DOMAIN]
    start_urls = [
        URL
    ]
    