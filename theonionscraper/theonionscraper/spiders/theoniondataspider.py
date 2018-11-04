from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import CrawlSpider, Rule, Spider
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from theonionscraper.items import TheOnionScraperItem
from theonionscraper.items import TheOnionDataItem
DOMAIN = 'theonion.com'
URL = 'http://%s' % DOMAIN
class OnionDataSpider(Spider):
    name = "onion_data_spider"
    allowed_domains = [DOMAIN]
    start_urls = [
        URL
    ]
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=False)
    