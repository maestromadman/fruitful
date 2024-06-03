from typing import Iterable
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class JojoSpider(CrawlSpider):
    #attributes
    name = "jojo"
    allowed_domains = "traderjoes.com"
    urls = ["traderjoes.com/home/products"]
    rules = (
        Rule(LinkExtractor(allow=(r"category\.php")), callback='parse_item', follow=True)
    )
    
    #method: start_requests -- 
   
    #method: parse
        

