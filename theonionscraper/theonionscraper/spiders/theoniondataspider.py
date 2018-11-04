from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import CrawlSpider, Rule, Spider
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from theonionscraper.items import TheOnionScraperItem
from theonionscraper.items import TheOnionDataItem
import scrapy
import csv
import re
DOMAIN = 'theonion.com'
URL = 'http://%s' % DOMAIN
class OnionDataSpider(Spider):
    def __init__(self, file='', **kwargs):
        self.start_urls = []
        with open('extras.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                self.start_urls.append(row[0])
        super().__init__(**kwargs)
    
    name = "onion_data_spider"
    allowed_domains = [DOMAIN]
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=False)
    
    def parse(self, response):
        # get the all paragraph element's text which is a child of a div
        # of class article__loader
        path_title = '//head/title[1]/text()'
        path_content = '//body//article/div[2]/div[1]/p/text()'
        article_title = response.xpath(path_title).extract()
        article_contents = response.xpath(path_content).extract()

        # add all texts to a single string to then create the vector used
        # to create a model
        str = ""
        for group in article_contents:
            str = str + group + " "

        # create the vector

        tSItem = TheOnionDataItem()
        tSItem["article"] = str
        tSItem["title"] = article_title
        tSItem["classification"] = 1

        return tSItem
