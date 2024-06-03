from typing import Iterable
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class Joe(scrapy.Spider):
    name = 'Joe'
    start_urls = ['https://www.traderjoes.com/home/products/pdp/fresh-mozzarella-cheese-snackers-070925']

    def start_requests(self):
        start_urls = ['https://www.traderjoes.com/home/products/pdp/fresh-mozzarella-cheese-snackers-070925']
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        yield {
            "title": response.xpath('//*[@id="spa-root"]/div[8]/div[1]/div/div[1]/div/div[2]/main/div/div/div[1]/div[1]/div/div[2]/h1').get(),
            "price": response.xpath('//*[@id="spa-root"]/div[8]/div[1]/div/div[1]/div/div[2]/main/div/div/div[1]/div[1]/div/div[2]/div[1]').get(),
            "calories": response.xpath('//*[@id="spa-root"]/div[8]/div[1]/div/div[1]/div/div[2]/main/div/div/div[2]/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/div/div[2]/div[2]').get(),
            "protein": response.xpath('//*[@id="spa-root"]/div[8]/div[1]/div/div[1]/div/div[2]/main/div/div/div[2]/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/table/tbody/tr[10]/td[2]').get()
        }
