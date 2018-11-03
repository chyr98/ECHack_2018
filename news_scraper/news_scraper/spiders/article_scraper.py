from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
import re
from news_scraper.items import theStarItem


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
        vector={}
        restrictions = [" ", ".", ",", "\"", "!", "?"]
        start = 0
        for i in range(len(str)):
            if str[i] in restrictions:
                if str[start:i] not in restrictions:
                    if str[start:i].lower() not in vector:
                        vector[str[start:i].lower()] = 0
                    vector[str[start:i].lower()] += 1
                start = i


        print(vector)
        tSItem = theStarItem()
        tSItem["vector"] = vector
        return vector
