from typing import Iterable
import scrapy
from scrapy_splash import SplashRequest

class Joe(scrapy.Spider):
    name = 'Joe'
    allowed_domains = ['traderjoes.com']
    start_urls = ['https://www.traderjoes.com/home']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 2})

    def parse(self, response):
        for product in response.xpath('//div[@class="product-category"]/div[@class="product-name"]'):
            yield {
                'heading':product.xpath('text()').get().strip()
            }
        print(product)
        

if __name__ == "__myspider__":
     object = Joe
     object.start_requests()
     object.parse()