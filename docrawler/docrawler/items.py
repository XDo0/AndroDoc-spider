# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DocrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
    api = scrapy.Field()
    func = scrapy.Field()
    para_name =scrapy.Field()
    para_val =scrapy.Field()
