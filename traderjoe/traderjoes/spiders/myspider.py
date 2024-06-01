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
        for title in response.xpath('/html/body/div/div[1]/div[1]/div/div[1]/div/div[2]/main/div/div/div[1]/div[1]/div/div/div[1]/section/h2'):
            yield {
                'heading': title.extract()
            }

if __name__ == "__myspider__":
     object = Joe
     object.start_requests()
     object.parse()