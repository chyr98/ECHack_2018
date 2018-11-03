from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
# from news_scraper.items import NewsScraperItem


class MySpider(BaseSpider):
    name = "craig"
    allowed_domains = ['thestar.com']

    # The URLs to start with
    start_urls = ['https://www.thestar.com/news/canada/2018/11/02/in-her-short-life-little-abby-inspired-countless-acts-of-kindness-now-even-strangers-are-mourning-her-death.html']
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        #titles = hxs.select("//span[@class='pl']")
        path = "//div[contains(@class,'article__body') and contains(@class, 'clearfix') and contains(@class,'article-story-body')]"
        sample = hxs.select(path).extract()[0]
        text = html2text.HTML2Text()
        text.ignore_links = True
        print("HELLO", text)
        # for title in titles:
        #     t = title.select("a/text()").extract()
        #     # link = titles.select("a/@href").extract()
        #     print(t)
