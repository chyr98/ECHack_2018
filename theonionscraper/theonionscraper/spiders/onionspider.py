from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from theonionscraper.items import TheOnionScraperItem
import scrapy
import requests
from lxml import html
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
                canonicalize=False
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
        links = LinkExtractor(canonicalize=False, unique=True).extract_links(response)
        items = []
        for link in links:
            validated = True
            allowed = False
            for ad in self.allowed_domains:
                if(ad in link.url):
                    allowed = True   
            if(allowed):
                link_page = requests.get(link.url) # get-request for the current link
                link_tree = html.fromstring(link_page.content) # builds the html/xml tree from the above opened link
                link_checks = link_tree.xpath(check_path)
            if (allowed) and (not(link_checks)):
                validated = False # link does not lead to an article
            if(allowed and validated):
                newitem = TheOnionScraperItem()
                newitem ['url'] = link.url
                items.append(newitem)
        return items # return list of scraped items which are urls to articles which can be data-scraped.
        

