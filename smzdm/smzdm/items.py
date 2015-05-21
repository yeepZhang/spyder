# -*- coding: utf-8 -*-

import scrapy


class SmzdmItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    brief = scrapy.Field()
    description = scrapy.Field()
    up = scrapy.Field()
    down = scrapy.Field()
    sitename = scrapy.Field()
    buylink = scrapy.Field()
    pass
