from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
import re
from news_scraper.items import NewsItem


class MySpider(BaseSpider):
    name = "craig"
    allowed_domains = ['thestar.com']

    # The URLs to start with
    start_urls = ['https://www.thestar.com/news/canada/2018/11/02/in-her-short-life-little-abby-inspired-countless-acts-of-kindness-now-even-strangers-are-mourning-her-death.html']
    def parse(self, response):

        # get the all paragraph element's text which is a child of a div
        # of class article__loader
        paths = '//div[contains(@class, "article__loader")]//div[p]/p/text()'
        texts = response.xpath(paths).extract()

        # add all texts to a single string to then create the vector used
        # to create a model
        str = ""
        for text in texts:
            str = str + text + " "

        # create the vector

        tSItem = NewsItem()
        tSItem["article"] = str
        tSItem["title"] = response.xpath('//h1[contains(@class, "article__headline")]/text()').extract()[0]
        tSItem["classification"] = 0

        return tSItem
