# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WyjobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    position=scrapy.Field()
    detail = scrapy.Field()
    corporation = scrapy.Field()
    base = scrapy.Field()
    sallary = scrapy.Field()
    date = scrapy.Field()

