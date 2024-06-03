# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TraderjoeItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    calories = scrapy.Field()
    protein = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)
