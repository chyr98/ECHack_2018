from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from theonionscraper.items import TheOnionScraperItem
import scrapy
DOMAIN = 'theonion.com'
URL = 'http://%s' % DOMAIN
class OnionSpider(CrawlSpider):
    name = 'onion_spider'
    allowed_domains = [DOMAIN]
    start_urls = [
        URL
    ]
    rules = [
        Rule(
            LinkExtractor(
                unique=True,
                canonicalize=True
            ),
            follow=True,
            callback="parse_item"
        )
    ]
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=False)
    
    def parse_item(self, response):
        check_path = '//head/meta[@content=\'article\']'
        links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
        items = []
        for link in links:
            allowed = False
            for ad in self.allowed_domains:
                if(ad in link.url):
                    allowed = True
            checks = response.xpath(check_path).extract()
            if not(checks):
                allowed = False # not an article
            if(allowed):
                newitem = TheOnionScraperItem()
                newitem ['url_from'] = link.url
                newitem ['url_to'] = response.url
                items.append(newitem)
        return items # return list of scraped items which are urls to articles which can be scraped.
        

