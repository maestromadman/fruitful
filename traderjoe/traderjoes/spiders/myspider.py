from typing import Iterable
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class Joe(scrapy.Spider):
    name = 'Joe'
    allowed_domains = ['traderjoes.com']
    start_urls = ['https://www.traderjoes.com/home/products/category/food-8']

    rules = (
        Rule(LinkExtractor(allow=(r"?filters=",))), Rule(LinkExtractor(allow=(r"/pdp",)), callback="parse_item"),
    )
    
    def parse_item(self, response):
        yield {
            #"title": response.css()
            #"price": response.css()
            #"calories": response.css()
            #"protein": response.css()
        }

if __name__ == "__myspider__":
     object = Joe
     object.start_requests()
     object.parse()